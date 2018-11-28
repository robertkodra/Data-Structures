# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [-1]
        self._data += [int(s) for s in input().split()]
        assert n == len(self._data) - 1

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def Parent(self, i):
        return i // 2

    def LeftChild(self, i):
        return 2*i

    def RightChild(self, i):
        return 2*i + 1

    def SiftDown(self, i):
        minIndex = i
        l = self.LeftChild(i)
        r = self.RightChild(i)
        # print("l is {}".format(l))
        # print("minIndex is {}".format(minIndex))
        if l <= len(self._data) - 1 and self._data[l] < self._data[minIndex]:
            minIndex = l
        # print("r is {}".format(r))
        if r <= len(self._data) - 1 and self._data[r] < self._data[minIndex]:
            minIndex = r
        if i != minIndex:
            self._swaps.append((i - 1, minIndex - 1))
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)

    def GenerateSwaps(self):
        for i in range((len(self._data) - 1) // 2, 0, -1):
            # print(self._data)
            self.SiftDown(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
