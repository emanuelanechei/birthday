##### Def #####
def check_input_date_format(x):
    if x in date_format_answer:
        return True
    else:
        return False

############################################################################################################
def input_birth_date():
    x = input("The date of your birthday: ")
    bad_input = True
    while bad_input:
        try:
            i = int(x)
            if i in dateList:
                bad_input = False
            else:
                print("Error! Invalid input.")
                x = input("The date of your birthday: ")
        except ValueError:
            print("Error! Invalid input.")
    if len(x) == 1:
        return '0' + x
    else:
        return x

def input_birth_month():
    x = input("The month of your birthday: ")
    bad_input = True
    while bad_input:
        try:
            i = int(x)
            if i in monthList:
                bad_input = False
            else:
                print("Error! Invalid input.")
                x = input("The month of your birthday: ")
        except ValueError:
            print("Error! Invalid input.")
    if len(x) == 1:
        return '0' + x
    else:
        return x

def input_birth_year():
    x = input("The year of your birthday (max year is 99,999): ")
    bad_input = True
    while bad_input:
        try:
            i = int(x)
            if i in yearList:
                bad_input = False
            else:
                print("Error! Invalid input.")
                x = input("The year of your birthday (max year is 99,999): ")
        except ValueError:
            print("Error! Invalid input.")
    if len(x) == 3:
        return '0' + x
    elif len(x) == 2:
        return '00' + x
    elif len(x) == 1:
        return '000' + x
    else:
        return x

############################################################################################################
'''def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False'''

############################################################################################################
def check_valid_date(date, month, year): #check if a date is valid (e.g: 31 Feb is INVALID)
    leap_year = int(year) / 4
    if int(month) == 2 and leap_year.is_integer() == True and int(date) >= 30:
        return False
    elif int(month) == 2 and leap_year.is_integer() == False and int(date) >= 29:
        return False
    else:
        return True

############################################################################################################
def digital_root(n): #sum all digits of a number into single digit or sth
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    elif x == 10 or x == 11 or x == 22:
        return x
    else:
        return digital_root(x)

############################################################################################################
def ruling_num_define(n): ##The meanings of the Ruling number
    if n == 2:
        print("\nOnly one total of numbers in the birth date will result in a Ruling Number 2, that is the total of 20."
              "\n(Totals of 29, 38 and 47 result in Ruling Number 11's.) Therefore, we find far fewer people with a Ruling"
              "\n2 (and Ruling 22/4) than any other of the Ruling Numbers. Not surprisingly, both Ruling Numbers suggest a"
              "\nspecial significance. The Ruling 2 is generally the sensitive, unassuming, supportive person, while the"
              "\nRuling 22/4 is far more assertive and self-confident."
              "\n\nRuling 2's are sensitive, intuitive, supportive, reliable, peacemaking, compassionate and artistic."
              "\n\nNotes for the 21st Century"
              "\nThe last Ruling 2 person to be born in the 20th century was on January 1, 1980. The first in the 21st"
              "\ncentury was born on 7/29/2000; thereafter many have and will be born. Thus, the sensitive nature of the"
              "\nRuling 2 will not be so unique, hopefully encouraging an increased movement toward intuitiveness and"
              "\npeace throughout the world."
              "\n\nFamous Ruling 2's"
              "\nPrince Philip born June 10, 1921"
              "\nRonald Reagan born February 6, 1911")

    elif n == 3:
        print("\nWhen we note its commanding position at the head of the mind plane, we realise why so much emphasis is"
              "\nplaced on thinking and on reasoning by people whose Ruling number is 3. These are people whose birth date"
              "\nnumbers total 12, 21, 30, 39 or 48."
              "\n\nThese people enjoy entertaining others, for they feel at home as the life of the party. Their minds"
              "\nare constantly alert and assessing, planning and thinking. They possess an intelligent sense of humour,"
              "\nyet often experience marriage problems."
              "\n\nFamous Ruling 3's"
              "\nBill Cosby born July 12, 1937"
              "\nFidel Castro born August 13, 1926"
              "\nKatharine Hepburn born November 9, 1909"
              "\nVivien Leigh born November 5, 1913")

    elif n == 4:
        print("\nIn the modern world, where so much general emphasis is placed on material concerns, the basic expression"
              "\nof most people with a Ruling 4 can be easily gratified. But there is more to them than materialism, though"
              "\ntheir major emphasis certainly lies on the physical, the 4 located in the centre of the physical plane."
              "\n\nRuling 4's are practical and conventional in outlook, often materialistic. They are interested in sports"
              "\nand very capable with their hands. They are doing people."
              "\n\nFamous Ruling 4's"
              "\nArnold Schwarzenegger born July 30, 1947"
              "\nPaul Hogan born October 8, 1939"
              "\nJoseph Stalin born December 21, 1879"
              "\nYasser Arafat born February 17, 1929"
              "\nElton John born March 25, 1947"
              "\nMartina Navratilova born October 18, 1956")

    elif n == 5:
        print("\nIn practice, we find that people with the Ruling Number 5 invariably strive to be free from constriction."
              "\nThis is a natural expression of their highly sensitive nature and their inherent need to express their feelings."
              "\nIt is not surprising when we realise that 5 is the centre of the Soul Plane and of the Arrow of the Will."
              "\nBirth dates whose component numbers total 14, 23, 32 or 41 have a Ruling Number 5."
              "\n\nTheir nature is essentially loving and freedom-loving, artistic, adventurous and moody, oscillating"
              "\nbetween joviality when free to be emotionally expressive and sullenness when feeling suppressed."
              "\nEssentially, they are ""feeling"" people."
              "\n\nFamous Ruling 5's"
              "\nAbraham Lincoln born February 12, 1809"
              "\nGreg Norman born February 10, 1955"
              "\nVincent van Gogh born March 30, 1853"
              "\nIrving Berlin born May 11, 1888"
              "\nAdolf Hitler born April 20, 1889"
              "\nJohnny Carson born October 23, 1925")

    elif n == 6:
        print("\nThis is a Ruling Number of extremes. These people have the potential for great creative power when living"
              "\npositively, yet they become incessant worriers when living negatively. The position of this number at the"
              "\ncentre of the Mind Plane and at the head of the Arrow of Will gives Ruling 6 people tremendous potential to"
              "\nperceive and create brilliantly. Regrettably, they rarely achieve lasting success in their lives due to their"
              "\never-present tendency to worry (their self-destruction). Birth dates with component numbers totalling 15, 24,"
              "\n33 or 42 have a Ruling Number 6."
              "\n\nRuling 6 people are creative, caring, just, unselfish, tolerant and home loving, but inclined toward"
              "\ndeep worry and extreme anxiety."
              "\n\nFamous Ruling 6's"
              "\nAgatha Christie born September 15, 1890"
              "\nSylvester Stallone born July 6, 1946"
              "\nMeryl Streep born June 22, 1949"
              "\nCharles de Gaulle born November 22, 1890"
              "\nJesse Jackson born October 8, 1941")

    elif n == 7:
        print("\nUnder the influence of this Ruling Number, people gain maximum experience from life's lesson book, both"
              "\nthrough the personal sacrifice of learning and through teaching or sharing (teaching being the consummate"
              "\nmeans of learning). Both facets of human growth are intimately related to physical expression, symbolised"
              "\nby the position of the 7 in the Birth Chart at the intersection of the Arrows of Practicality and Activity."
              "\nBirth dates with component numbers totalling 16, 25, 34 and 43 have a Ruling Number 7."
              "\n\nRuling 7's need to learn through personal experience, but dislike external discipline. They are assertive,"
              "\nphilosophical and humanitarian. Their lives incur an unusually high level of sacrifice."
              "\n\nFamous Ruling 7's"
              "\nMarilyn Monroe born June 1, 1926"
              "\nPeter Tchaikovsky born May 7, 1840"
              "\nCole Porter born June 9, 1891"
              "\nConrad Hilton born December 25, 1887"
              "\nGermaine Greer born January 29, 1939")

    elif n == 8:
        print("\nThese are people who regard independence as one of the most important aspects of life. They can be very"
              "\ncomplex people who invariably possess great wisdom and strength or character. Their power derives from the"
              "\nposition of the 8 as the number of wisdom on the soul plane, as well as being in the centre of the Arrow of"
              "\nActivity. Ruling number 8 birth dates are those that total 17, 26, 35 or 44."
              "\n\nThey are independent, highly dependable, self-confident, undemonstrative, commercially oriented and"
              "\ndeeply concerned for the sick and the helpless."
              "\n\nFamous Ruling 8's"
              "\nJoan Collins born May 23, 1933"
              "\nElizabeth Taylor born February 27, 1932"
              "\nBoris Yeltsin born February 1, 1931"
              "\nNelson Mandela born July 18, 1918"
              "\nPaul Newman born January 5, 1946"
              "\niza Minnelli born March 12, 1946"
              "\nJane Fonda born December 21, 1937")

    elif n == 9:
        print("\nThe humanitarian qualities of ambition, responsibility and idealism are the three-fold aspects of Ruling 9"
              "\npeople, whose prime motivation is to put people before things. They are individuals whose birth date numbers"
              "\ntotal 18, 27, 36 or 45."
              "\n\nRuling 9's are eminently responsible, extremely honest, idealistic, ambitious, humanitarian and very serious"
              "\nabout life. They have difficulty saving money."
              "\n\nFamous Ruling 9's"
              "\nShirley Maclaine born April 24, 1934"
              "\nlvis Presley born January 8, 1935"
              "\nLinda Evans born November 18, 1942"
              "\nBurt Lancaster born November 2, 1913"
              "\nJimmy Carter born October 1, 1924"
              "\nRichard Harris born October 1, 1933")

    elif n == 10:
        print("\nMost Ruling Numbers can be expressed in a variety of ways, depending on the degree of awareness of the"
              "\nperson. But there is no greater range of expression than that found in the potential of the Ruling 10. They"
              "\nvary from the most likable, personality-plus people when living positively, to lost, floundering, insecure"
              "\nbeings when negativity takes over. They are the most adaptable people. They have the potential for brilliant"
              "\nsuccess or they can languish in mediocrity. Birth dates with totals of 19, 28, 37 or 46 are Ruling 10's."
              "\n\nThey are confident, debonair, bright and happy people, with an extremely sensitive touch and an amazing"
              "\nability to sell."
              "\n\nFamous Ruling 10's"
              "\nRupert Murdoch born March 11, 1931"
              "\nJack Nicholson born April 22, 1937"
              "\nSophia Loren born September 20, 1943"
              "\nHenry Ford born July 30, 1863"
              "\nJerry Lewis born March 16, 1926"
              "\nBilly Joel born May 9, 1949")

    elif n == 11:
        print("\nAn especially high level of spirituality surrounds this Ruling Number, offering those born to it a unique"
              "\npotential for developing the awareness of the high self. Unfortunately, more people fail to live up to this"
              "\npotential power than develop it, but this pattern is changing with the rapid approach of the New Age of"
              "\nenlightenment (New Age). Though we do not find many Ruling 11's as most of the other numbers, they certainly"
              "\nproliferate in domains where personal growth and spiritual upliftment predominate (and they will all be reading"
              "\nthis book!). In practice, only two birth date totals commonly qualify for Ruling number 11 – that is, 29"
              "\nand 38 – though an occasional birth date total of 47 will be found."
              "\n\nSensitive, feeling and caring people are the Ruling 11's. They love refinement, beauty and everything"
              "\nwith a depth of cultural substance; and are intensely honest and compassionate, often preferring to avoid"
              "\nthe life of hard business, for they are generally not competent money managers."
              "\n\nFamous Ruling 11's"
              "\nWolfgang Amadeus Mozart born January 27, 1756"
              "\nPrince Charles born November 14, 1948"
              "\nAnthony Newley born September 24, 1931"
              "\nJacqueline Kennedy Onassis born July 28, 1929"
              "\nTony Bennett born August 3, 1926"
              "\nSir Edmund Hillary born July 20, 1919"
              "\nJohn Glenn born July 18, 1921"
              "\nEartha Kitt born January 26, 1928")

    elif n == 22:
        print("\nThis is the master number. People born as 22/4's have almost limitless potential and often make their mark"
              "\nin life by achieving seemingly impossible goals. But there are two distinctly different Ruling 22/4's – the"
              "\naware and the unaware. The difference between them is as extreme as the power of the number. The former benefit"
              "\nfrom the successful mastery of any aspect of life into which they are directed; the latter drift into a lazy"
              "\nindifference, becoming almost useless misfits, many of them drifting into mental institutions. Only one total"
              "\nof birth date numbers resolves to a Ruling Number 22/4 and that is the total of 22, occurring only with some"
              "\none to two percent of the population."
              "\n\nThis is the master number whose bearers have the most responsibility to humanity. They are self-confident,"
              "\nhighly intuitive and sensitive, with a tight rein on their emotions and an intense concern for human welfare."
              "\nThey have to take care not to become ruthless in their pursuit of their goals."
              "\n\nFamous Ruling 22/4's"
              "\nMargaret Thatcher born October 13, 1925"
              "\nRichard Wagner born May 22, 1813"
              "\nFrank Sinatra born December 12, 1915"
              "\nLuciano Pavarotti born October 12, 1935"
              "\nClint Eastwood born May 31, 1930")

############################################################################################################
def continue_yn():
    y_input = ["y", "Yes", "yes"]
    n_input = ["n", "No", "no"]
    x = input("\nContinue? [y/n] ")
    bad_input = True
    while bad_input:
        try:
            if x in y_input or x in n_input:
                bad_input = False
            else:
                print("Error! Invalid input.")
                x = input("Continue? [y/n] ")
        except ValueError:
            print("Error! Invalid input.")
    if x in n_input:
        exit()

############################################################################################################
##### Infinite year list #####
'''year = 1
keep_going = True
while keep_going:
    year += 1
    if year == 10e10:
        keep_going = False'''

##### List #####
date_format_answer = ["a", "b", "c", "A", "B", "C"]

dateList =[]
for i in range(1, 32):
    dateList.append(i)

monthList = []
for i in range(1, 13):
    monthList.append(i)

yearList = []
for i in range(1, int(10e5)):   #It was the infinite year list
    yearList.append(i)          #Cannot make an infinite list
                                #It has taken foreverrrr since 10e10 or 10^10
