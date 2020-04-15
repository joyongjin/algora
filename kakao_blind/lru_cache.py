class Node:
    def __init__(self, key, _next=None, _prev=None):
        self.key = key
        self.next = _next
        self.prev = _prev

    def __str__(self):
        return self.key

    def set_next(self, node):
        self.next = node
        node.prev = self

    def set_prev(self, node):
        self.prev = node
        node.next = self


class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = Node('head')  # recently
        self.tail = Node('tail')  # older
        self.keys = dict()
        self.size = 0

    def hit(self, key):
        """
        캐시 내에 값이 있다면, head 로 옮긴 뒤, 1초 리턴
        캐시 내에 값이 없다면, head 에 추가한 뒤, 5초 리턴
        """
        if self.max_size == 0:  # 캐시 사이즈 자체가 0이라면, 로직 탈 필요 없음.
            return 5

        key = key.lower()  # 대소문자 구분 X
        node = self.keys.get(key)
        if node is None:  # 없는 경우
            self.append(key)
            cost = 5
        else:  # 있는 경우
            node.next.set_prev(node.prev)
            node.set_next(self.head.next)
            node.set_prev(self.head)
            cost = 1
        return cost

    def append(self, key):
        """
        새로운 key 를 기반으로 node 를 생성 후, 추가해준다.
        """
        node = Node(key)
        if self.size == 0:
            # 사이즈 자체가 0이라면, 생성한 노드의 next 는 tail 임.
            to_next = self.tail
        else:
            if self.size == self.max_size:
                # 사이즈가 가득 찼다면, pop
                self.pop()
            # 그 외엔, 생성한 노드의 next 는 기존의 head.next 임.
            to_next = self.head.next

        node.set_next(to_next)
        node.set_prev(self.head)
        self.keys[key] = node
        self.size += 1
        return node

    def pop(self):
        """
        가장 마지막 (tail.prev) 항목을 제거한다.
        """
        if self.size > 0:
            target = self.tail.prev
            self.tail.set_prev(target.prev)
            self.keys.pop(target.key)
            self.size -= 1
            return True
        else:
            return False


def solution(cacheSize, cities):
    cache = Cache(cacheSize)
    answer = 0
    for city in cities:
        answer += cache.hit(city)
    return answer


if __name__ == '__main__':
    def check(label, size, cities, expect):
        "{} 결과: {} / 기대: {}".format(label, solution(size, cities), expect)


    check('테스트 1', 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 50)
    check('테스트 1', 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "Pangyo"], 50)
