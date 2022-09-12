print('''
\t\t\t\tPersonal Dictionary

''')
pers_dic = {}
while(True):
    print("\t\t\t\t1.Add a word with its meaning")
    print("\t\t\t\t2.Delete a word")
    print("\t\t\t\t3.Display all words")
    print("\t\t\t\t4.Search a word")
    print("\t\t\t\t5.Exit")
    s = int(input("\t\tEnter your choice: "))
    match s:
        case 1:
                 w = input("Enter the word: ")
                 m = input("Enter its meaning: ")
                 dic = { w : m }
                 pers_dic.update(dic)
                 print("Word saved successfully.")
        case 2:
                w = input("Enter the word: ")
                if w in pers_dic.keys():      
                    del pers_dic[w]
                    print("Word deleted successfully.")
                else:
                    print("Word not found!!!")
        case 3:
               if len(pers_dic) == 0:
                print('Dictionary is empty.')
               else:
                print('Words in the dictionary are -:')
                print()
                i = 1
                for key, item in pers_dic.items():
                    print(f'{i}.{key}  :  {item}')
                    print()
                    i+=1
        case 4:
                 w = input("Enter the word: ")
                 if w in pers_dic.keys():
                    for key, item in pers_dic.items():
                        if key==w:
                          print(f'{key}  :  {item}')
                          break
                 else:
                    print('Word not found!!!')
        case 5:
                quit()
        case default:
                print("Invalid choice!!!")
    print()
    s = input("Press enter to continue...")

