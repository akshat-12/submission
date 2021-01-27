import datetime
import calendar
def D(date_dic):
    return_dict = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
    tabs = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
    list_days = return_dict.keys()
    list_days = list(list_days)
    for date in date_dic:
        k = int(date[8]+date[9])
        m = int(date[5]+date[6])
        Y = int(date[0]+date[1]+date[2]+date[3])
        F = calendar.weekday(Y, m, k)
        if F == 6:
            tabs["Sun"] = tabs["Sun"]+1
            return_dict["Sun"] = return_dict["Sun"] + date_dic[date]
        elif F == 0:
            tabs["Mon"] = tabs["Mon"]+1
            return_dict["Mon"] = return_dict["Mon"] + date_dic[date]
        elif F == 1:
            tabs["Tue"] = tabs["Tue"]+1
            return_dict["Tue"] = return_dict["Tue"] + date_dic[date]
        elif F == 2:
            tabs["Wed"] = tabs["Wed"]+1
            return_dict["Wed"] = return_dict["Wed"] + date_dic[date]
        elif F == 3:
            tabs["Thu"] = tabs["Thu"]+1
            return_dict["Thu"] = return_dict["Thu"] + date_dic[date]
        elif F == 4:
            tabs["Fri"] = tabs["Fri"]+1
            return_dict["Fri"] = return_dict["Fri"] + date_dic[date]
        elif F == 5:
            tabs["Sat"] = tabs["Sat"]+1
            return_dict["Sat"] = return_dict["Sat"] + date_dic[date]
    zeros_list = []
    for day in tabs:
        if tabs[day] == 0:
            zeros_list.append(0)
        else:
            zeros_list.append(1)
    cons_zeros = []
    for i in range(7):
        if zeros_list[i] == 0:
            j = i
            tempcount = 0
            while zeros_list[j] == 0:
                tempcount = tempcount + 1
                j = j + 1
            if tempcount > 1:
                cons_zeros.append([i,tempcount])    
    for entry in cons_zeros:
        num = entry[1]
        start = entry[0]
        s = - return_dict[list_days[start-1]] + return_dict[list_days[start+num]]
        dif = s/(num+1)
        
        for index in range(start,start+num):
            return_dict[list_days[index]] = int(return_dict[list_days[index-1]] + dif)
    
    for i in range(7):
        if return_dict[list_days[i]] == 0 and tabs[list_days[i]] == 0:
            return_dict[list_days[i]] = int((return_dict[list_days[i-1]] + return_dict[list_days[i+1]])/2)
    
    return return_dict

print(D({'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}))
print(D({'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}))
