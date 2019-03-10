condition="y"
daylist=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
monthlist=["January","February","March","April","May","June","July","August","September","October","November","December"]
daynum=[31,28,31,30,31,30,31,31,30,31,30,31]
def dayct(y):
    daycnt=0
    for i in range(1900,y):
                if(((i%4==0)&(i%100!=0))or (i%400==0)):
                        daycnt=daycnt+366
                        
                else:
                    daycnt=daycnt+365
    return daycnt
#jan 1900 is a monday
start=0
flag=0
tot=""
linee=""
for i in daylist:
       tot=tot+i+"\t"
       linee=linee+"--------"
while (condition=="y"):
        print("\nCalendar Program (for years above 1900)")
        option=int(input("The availiable options are:- \n1-Print calendar of a year \n2-Print calendar of given month\n3-No of days between 2 dates\n4-Day of the diven date\n\nEnter your option : "))
        if option==1 :
            year=int(input("Enter a year : "))
            daycount=dayct(year)
            firstday=daycount%7
            k=firstday
            if (((year%4==0)&(year%100!=0))or (year%400==0)):
                daynum[1]=29
            for n in range (12):
                print ("\n\n\t\t",monthlist[n],year)
                print (linee)
                print (tot)
                print (linee)
                space="\t"*k
                print (space,end=" ")
                day=1
                while (day<=daynum[n]):
                    flag=0
                    line=""
                    for j in range(k,7):
                        line+=str(day)+"\t"
                        if (day==daynum[n]) :
                            flag=1
                            k=j+1
                            break
                        day=day+1
                    if (flag==1):
                        print(line)
                        break
                    else:
                        print(line,"\n")
                        k=0
        elif option==2:
            year=int(input("Enter a year : "))
            mm=int(input("Enter the month : "))
            print ("\n\n\t\t",monthlist[mm-1], year)
            print (linee)
            print (tot)
            print (linee)
            daycount=dayct(year)   
            firstday=daycount%7
            k=firstday
            if (((year%4==0)&(year%100!=0))or (year%400==0)):
                daynum[1]=29
            for n in range (12):
                    space="\t"*k
                    if(n==mm-1):        
                        print (space,end=" ")
                    day=1
                    while (day<=daynum[n]):
                        flag=0
                        line=""
                        for j in range(k,7):
                            line+=str(day)+"\t"
                            if (day==daynum[n]) :
                                flag=1
                                k=j+1
                                break
                            day=day+1
                        if (flag==1):
                            if (n==mm-1):
                             print(line)
                            break
                        else:
                            if (n==mm-1):
                             print (line,"\n")
                            k=0


         
        elif option==3 :
            sdate=input("Enter the starting date in (dd/mm/yyyy) format : ")
            edate=input("Enter the ending date in (dd/mm/yyyy) format : ")
            day=0
            flag=0
            def date(date):
                return int(date[:2]),int(date[3:5]),int(date[6:])
            d1,m1,y1=date(sdate)
            d2,m2,y2=date(edate)
            if (y1==y2):
                if (m1==m2):
                    day=d2-d1+1
                else:
                    for i in range(d1,daynum[m1-1]+1):
                        day=day+1
                    for i in range(m1+1,m2):
                        day=day+daynum[i]
                    for i in range(1,d2):
                        day=day+1
            else:
                for i in range(d1,daynum[m1-1]+1):
                    day=day+1
                for i in range(m1,12):
                    day=day+daynum[i]
                    if (((y1%4==0)&(y1%100!=0))|(y1%400==0))and (i==1):
                        day=day+1
                for i in range(y1+1,y2):
                    if (((i%4==0)&(i%100!=0))|(i%400==0)):
                        day=day+366
                    else:
                        day=day+365
                for i in range(m2-1):
                    day=day+daynum[i]
                    if (((y2%4==0)&(y2%100!=0))|(y2%400==0))and (i==1):
                        day=day+1
                for i in range(1,d2+1):
                    day=day+1
            print ("\nIncluding Start/End : ",(day),"\nExcluding Start/End: ",(day-2))
            

        elif option==4:
            dd=int(input("Enter the date : "))
            mm=int(input("Enter the month : "))
            yyyy=int(input("Enter the year : "))
            daycount=dayct(yyyy) 
            daycount-=1
            for i in range(0, mm-1):
                daycount+=daynum[i]
            for i in range(0,dd):
                    daycount=daycount+1
            if(((yyyy%4==0)&(yyyy%100!=0))or (yyyy%400==0)):
                if(mm>2):
                    daycount=daycount+1
            print ("It is a",daylist[daycount%7])
        else :
            print ("Invalid Option")

        condition=input("\n\nDo you want to continue Press (y/n) : ")
        condition=condition.lower()
        if (condition!="y"):
            print ("Program ended")