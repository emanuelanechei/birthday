# Hello, this is the chief. The one that was so bored during the coronavirus shit. My name is Huỳnh Nguyên Huy Hoàng
# Call me Hoàng. That is my official name, or other names: Quoàng, Henry. All this stuff is only used for personal purposes.
# Just recently I found about the NUMEROLOGY
'''(Numerology is any belief in the divine or mystical relationship between a number and one or more coinciding events.
It is also the study of the numerical value of the letters in words, names, and ideas. It is often associated with the
paranormal, alongside astrology and similar divinatory arts ~ Wikipedia :D)'''
# #


import formulas as formu
############################################################################################################
valid_date = False
valid_input = False


print("NUMEROLOGY")
##### Input birthday with a chosen date format #####
date_format = input("\n(a) DD/MM/YYYY" \
                    "\n(b) YYYY/MM/DD" \
                    "\n(c) MM/DD/YYYY" \
                    "\nSelect your date format: ")


############################################################################################################
while valid_input == False:
    #FORCE to input aA, bB or cC to answer
    if formu.check_input_date_format(date_format) == True:
        valid_input = True
        if date_format == "a" or date_format == "A":
            #Input birthday with the chosen format
            birth_date = formu.input_birth_date()
            birth_month = formu.input_birth_month()
            birth_year = formu.input_birth_year()
            #Loop to check if the input is a valid date
            formu.check_valid_date(birth_date, birth_month, birth_year)
            while valid_date == False:
                if formu.check_valid_date(birth_date, birth_month, birth_year) == True:
                    valid_date == True
                    print("\nYour birthday is " + birth_date + "/" + birth_month + "/" + birth_year)
                    break
                else:
                    print("Invalid date!")
                    birth_date = formu.input_birth_date()
                    birth_month = formu.input_birth_month()
                    birth_year = formu.input_birth_year()


############################################################################################################
        elif date_format == "b" or date_format == "B":
            birth_year = formu.input_birth_year()
            birth_month = formu.input_birth_month()
            birth_date = formu.input_birth_date()
            formu.check_valid_date(birth_date, birth_month, birth_year)
            while valid_date == False:
                if formu.check_valid_date(birth_date, birth_month, birth_year) == True:
                    valid_date == True
                    print("\nYour birthday is " + birth_year + "/" + birth_month + "/" + birth_date)
                    break
                else:
                    print("Invalid date!")
                    birth_year = formu.input_birth_year()
                    birth_month = formu.input_birth_month()
                    birth_date = formu.input_birth_date()
                    formu.check_valid_date(birth_date, birth_month, birth_year)


############################################################################################################
        elif date_format == "c" or date_format == "C":
            birth_month = formu.input_birth_month()
            birth_date = formu.input_birth_date()
            birth_year = formu.input_birth_year()
            formu.check_valid_date(birth_date, birth_month, birth_year)
            while valid_date == False:
                if formu.check_valid_date(birth_date, birth_month, birth_year) == True:
                    valid_date == True
                    print("\nYour birthday is " + birth_month + "/" + birth_date + "/" + birth_year)
                    break
                else:
                    print("Invalid date!")
                    birth_year = formu.input_birth_year()
                    birth_month = formu.input_birth_month()
                    birth_date = formu.input_birth_date()
                    formu.check_valid_date(birth_date, birth_month, birth_year)


        ####################################################################################################
    else:
        print("Invalid input!")
        date_format = input("\n(a) DD/MM/YYYY" \
                            "\n(b) YYYY/MM/DD" \
                            "\n(c) MM/DD/YYYY" \
                            "\nSelect your date format: ")


############################################################################################################
birhtday = birth_date + birth_month + birth_year


#List of the birthday digits
birth_digit = [int(x) for x in str(birhtday)]


#Calculate the Ruling number
ruling_num = formu.digital_root(birhtday)
if ruling_num != 22:
    print("Your ruling number is " + str(ruling_num))
else:
    print("Your ruling number is " + str(ruling_num) + "/4")


#The meanings of the Ruling number
formu.ruling_num_define(ruling_num)
print("~D. A. Phillips, The Complete Book of Numerology. Hay House, 2005.~")


formu.continue_yn() #Do you want to continue?


#Pythagorean Birth chart
print("Pythagorean Birth chart")
print("3     6     9   MIND PLANE (mental, thinking)")

print("\n2     5     8   SOUL PLANE (spiritual, feeling)")

print("\n1     4     7   PHYSICAL PLANE (pratical, doing)")


#Birth Chart Examples
print("\nExample 1: a person has a birth date of May 27th, 1983")
print("3     _     9")
print("\n2     5     8")
print("\n1     _     7")

print("\nExample 2: a person has a birth date of November 11th, 1999")
print("_____     _____      999 ")
print("\n_____     _____     _____")
print("\n11111     _____     _____")

print("\nExample 3: a person has a birth date of February 20th, 2000")
print("___     ___     ___")
print("\n222     ___     ___")
print("\n___     ___     ___")


formu.continue_yn() #Do you want to continue?


one = birth_digit.count(1)
two = birth_digit.count(2)
three = birth_digit.count(3)
four = birth_digit.count(4)
five = birth_digit.count(5)
six = birth_digit.count(6)
seven = birth_digit.count(7)
eight = birth_digit.count(8)
nine = birth_digit.count(9)

# The Arrows of Individuality
if one != 0 and five != 0 and nine != 0:  # 1
    deter = True
    print("Arrow of DETERMINATION, due to the PRESENT of 1, 5 & 9")
else:
    deter = False
if one == 0 and five == 0 and nine == 0:  # 2
    procras = True
    print("Arrow of PROCRASTINATION, due to the ABSENCE of 1, 5 & 9")
else:
    procras = False
if three != 0 and five != 0 and seven != 0:  # 3
    spirit = True
    print("Arrow of SPIRITUALITY, due to the PRESENT of 3, 5 & 7")
else:
    spirit = False
if three == 0 and five == 0 and seven == 0:  # 4
    enquirer = True
    print("Arrow of THE ENQUIRER (or originally as the Arrow of Scepticism), due to the ABSENCE of 3, 5 & 7")
else:
    enquirer = False
if three != 0 and six != 0 and nine != 0:  # 5
    intellect = True
    print("Arrow of THE INTELLECT, due to the PRESENT of 3, 6 & 9")
else:
    intellect = False
if three == 0 and six == 0 and nine == 0:  # 6
    poor_mem = True
    print("Arrow of POOR MEMORY, due to the ABSENCE of 3, 6 & 9")
else:
    poor_mem = False
if two != 0 and five != 0 and eight != 0:  # 7
    emo_balance = True
    print("Arrow of EMOTIONAL BALANCE, due to the PRESENT of 2, 5 & 8")
else:
    emo_balance = False
if two == 0 and five == 0 and eight == 0:  # 8
    hypersens = True
    print("Arrow of HYPERSENSITIVITY, due to the ABSENCE of 2, 5 & 8")
else:
    hypersens = False
if one != 0 and four != 0 and seven != 0:  # 9
    practi = True
    print("Arrow of PRACTICALITY, due to the PRESENT of 1, 4 & 7")
else:
    practi = False
if one == 0 and four == 0 and seven == 0:  # 10
    disorder = True
    print("Arrow of DISORDER, due to the ABSENCE of 1, 4 & 7")
else:
    disorder = False
if one != 0 and two != 0 and three != 0:  # 11  No mention about absence of 1, 2 and 3
    planner = True
    print("Arrow of THE PLANNER, due to the PRESENT of 1, 2 & 3")
else:
    planner = False
if four != 0 and five != 0 and six != 0:  # 12
    will = True
    print("Arrow of THE WILL, due to the PRESENT of 4, 5 & 6")
else:
    will = False
if four == 0 and five == 0 and six == 0:  # 13
    frustra = True
    print("Arrow of FRUSTRATION, due to the ABSENCE of 4, 5 & 6")
else:
    frustra = False
if seven != 0 and eight != 0 and nine != 0:  # 14
    activity = True
    print("Arrow of ACTIVITY, due to the PRESENT of 7, 8 & 9")
else:
    activity = False
if seven == 0 and eight == 0 and nine == 0:  # 15
    passivity = True
    print("Arrow of PASSIVITY, due to the ABSENCE of 7, 8 & 9")
else:
    passivity = False

'''Honestly I have no idea how to optimize this part (less code lines)'''

# No arrow
if deter == False and procras == False and spirit == False and enquirer == False and intellect == False and poor_mem == False and emo_balance == False and hypersens == False and practi == False and disorder == False and planner == False and will == False and frustra == False and activity == False and passivity == False:
    print("BIRTH CHARTS WITH NO ARROW")