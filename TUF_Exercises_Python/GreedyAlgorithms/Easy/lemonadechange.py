def lemonadeChange(bills: list) -> bool:
    fives, tens = 0,0 #Initialize fives and tens to 0
    for bill in bills: #Iterate each bill value in bills
        if bill == 5: #If bill value = 5, then increment fives by 1
            fives+=1
        elif bill == 10: #If bill value = 10, check if fives is present for change if not return False, if yes then decrement by 1 and increment tens by 1
            if fives==0:
                return False
            fives-=1
            tens+=1
        else:
            if bill == 20: #If bill value is 20 then check if tens and fives value is 1 or above then 20-10-5 could be done
                if tens>0 and fives>0:
                    fives-=1
                    tens-=1
                elif fives>=3: #If there are no tens and only fives check if 3*fives = 15 is there, if not then return False
                    fives-=3
                else:
                    return False
    return True

if __name__=="__main__":
    bills = [5,5,5,10,20]
    print(lemonadeChange(bills))

    bills = [5,5,10,10,20]
    print(lemonadeChange(bills))

#Time Complexity: O(n)
#Space Complexity: O(1)