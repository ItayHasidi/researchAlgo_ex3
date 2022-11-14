class List(list):
    def __init__(self, data):
        self.data: List = data

    def __getitem__(self, index):  # operator[] for reading
        list_index = []
        if isinstance(index, int):
            list_index = self.data[index]
        else:
            for i in index:
                if not isinstance(list_index, int):
                    if len(list_index) == 0:
                        list_index = self.data[i]
                    else:
                        list_index = list_index[i]
        return list_index

    def __setitem__(self, index, value: object) -> None:  # operator[] for writing
        i0: int = index[0]
        i1: int = index[1]
        i2: int = index[2]
        print(type(self.data))
        print(self.data[i0, i1, i2])
        self.data[index[0], index[1], index[2]] = value


if __name__ == '__main__':
    mylist = List(
        [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], ])
    print(mylist[0, 1, 3])
    print(mylist[0])
    # mylist[0] = 88
    mylist[0, 1, 3] = 88
    print(mylist[0, 1, 3])
    print(mylist.data)

