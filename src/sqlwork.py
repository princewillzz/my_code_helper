
def take_data():
    words = []
    try:
        while True:
            line = input(":- ")
            if line == None or line.isspace() or len(line) == 0:
                print("done")
                break
            word_list  = line.split(" ")
            for word in word_list:
                words.append(word)
    except:
        words = None

    return words


def count_question_mark(sql: str):
    count = 0
    try:
        for ch in sql:
            if ch == '?':
                count+=1
    except:
        count = 0
    return count


def show_queries(words: list, sql: str, count_of_question_mark: int):
    try:
        i = 0
        length_of_words = len(words)
        while i < length_of_words:
            query = sql
            for index in range(0, count_of_question_mark):
                if i >= length_of_words:
                    return
                if words[i].isnumeric():
                    query = query.replace('?', words[i], 1)
                else :
                    query = query.replace('?', f'"{words[i]}"', 1)
                i+=1
            print(query)
    except:
        print("something went wrong")


def generateSQLQueries():
    try:
        sql = input("Enter the sql query: ")
        print("Now Enter all Data(ENTER🔑 to break): ")

        # Count question marks
        count = count_question_mark(sql)
        if count <= 0:
            print("No places to replace the data")
            return None
        # take all the data
        words = take_data()
        if words == None:
            print("No data to be replaced with placeholders")
            return None
        print("\n")
        show_queries(words, sql, count)
        print("\n")
    except:
        print("something went wrong")

