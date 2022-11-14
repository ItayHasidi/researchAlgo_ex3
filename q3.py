class List(list):
    def __init__(self, data):
        self.data: List = data

    def __getitem__(self, index):  # operator[] for reading
        list_index = []
        if isinstance(index, int):
            list_index = self.data[index]
        else:
            for i in index:
                print(type(list_index), type("int"))
                if type(list_index) != type(int) and len(list_index) == 0:
                    list_index = self.data[i]
                else:
                    list_index = list_index[i]
        return list_index

    def __setitem__(self, index, value: object) -> None:  # operator[] for writing
        # list_index = []
        # for i in index:
        #     if len(list_index) == 0:
        #         list_index = self.data[i]
        #     else:
        #         list_index = list_index[i]
        # list_index = value
        self.data[index] = value


if __name__ == '__main__':
    mylist = List(
        [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], ])
    print(mylist[0, 1, 3])
    print(mylist[0])
    mylist[0] = 88
    print(mylist[0, 1, 3])
