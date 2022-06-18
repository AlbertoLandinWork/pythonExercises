def remove_duplicates(some_list):
    without_duplicates = list()
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1,1,2,2,2,3,4,5]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

# Reto
print(list(set([1,1,2,2,2,3,4,5])))