class List(list):
    def __init__(self, data):
        self.data: List = data

    def __getitem__(self, index):
        """
        operator[] for reading

        >>> lst = List([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
        >>> lst[0, 0, 0]
        0

        >>> lst = List([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
        >>> lst[0] = [[10, 11], [12, 13]]
        >>> lst[0]
        [[10, 11], [12, 13]]

        >>> lst = List([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
        >>> lst[0, 0] = [10, 11]
        >>> lst[0]
        [[10, 11], [2, 3]]

        >>> lst = List([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
        >>> lst[0, 0] = [10, 11]
        >>> lst[0, 0]
        [10, 11]
        """
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
        if isinstance(index, int):
            self.data[index] = value
        else:
            i = 0
            idx = index[i]
            i += 1
            list_index = self.data[idx]
            while i < len(index) - 1:
                idx = index[i]
                if not isinstance(list_index, int):
                    list_index = list_index[idx]
                i += 1
            idx = index[i]
            i += 1
            list_index[idx] = value


if __name__ == '__main__':
    mylist = List(
        [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], ])
    print(mylist[0, 1, 3])
    print(mylist[0])
    mylist[0, 1, 3] = 88
    print(mylist[0, 1, 3])
    print(mylist.data)

