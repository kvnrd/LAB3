from AVL import Node, AVLTree
from RedBlackTree import RBTNode, RedBlackTree

count = 0
max_word = ""
max_count = 0
counter = 0

def load_AVL(file):
    word_tree = AVLTree()


    for line in file:
        word = line.strip("\n")
        word_tree.insert(Node(word))
    file.close()

    return word_tree


def load_RBT(word_file):
    word_tree = RedBlackTree()


    for line in word_file:
        word = line.strip("\n")
        word_tree.insert(word)
    word_file.close()

    return word_tree


def print_anagrams(word, treeType, prefix=""):

    global count
    if len(word) <=1:
        str = prefix + word

        if treeType.search(str):
            count = count + 1
            print(prefix+word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if cur not in before:
                print_anagrams(before + after, treeType, prefix + cur)


def traverse_tree(root, tree):
    if root == None:
        return None
    traverse_tree(root.left, tree)
    biggestWord(root.key, tree)
    traverse_tree(root.right, tree)


def find_max(word, treetype, prefix=""):
    global counter
    global max_word
    global max_count



    if len(word) <=1:
        str = prefix + word

        if treetype.search(str):
            counter = counter + 1
    else:

        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if cur not in before:
                find_max(before + after, treetype, prefix + cur)


def biggestWord(word, treetype):
    global counter
    global max_word
    global max_count

    find_max(word, treetype)

    if counter > max_count:
        max_count = counter
        max_word = word
        counter = 0

    counter = 0




def search_word(word, tree):

    if tree.search(word):
        print("Word found!")
    else:
        print("Word is not in the tree")

def main():
    word_file = open("test1.txt", "r")

    print("********************************MENU********************************\n")

    answer = input("Select the type of tree you want to use: \n1. AVL Tree \n2. Red Black Tree")


    if answer == "1":
        avl_words = load_AVL(word_file)
        word = input("What word would you like to search for?")
        search_word(word, avl_words)
        anagram = input("Which word do you want to permutate?")
        print_anagrams(anagram, avl_words)
        print("Number of permutations in word file: ", count)
        traverse_tree(avl_words.root, avl_words)
        print("----------------------------------------------------")
        print(max_word, "Number of permutations in tree: ",max_count)

    elif answer =="2":

        rbt_words = load_RBT(word_file)
        word = input("What word would you like to search for?")
        search_word(word, rbt_words)
        anagram = input("Which word do you want to permutate?")
        print_anagrams(anagram, rbt_words)
        print("Number of permutations in word file: ", count)
        traverse_tree(rbt_words.root, rbt_words)
        print("----------------------------------------------------")
        print(max_word, "Number of permutations in tree: ", max_count)




main()