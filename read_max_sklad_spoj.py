# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import scipy as sc

print("poczatke wczytywania")
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
#H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print("koniec wczytywania")

#assortatywnośc 1
#temp = nx.degree_assortativity_coefficient(H)
#print(temp)
#print("drugie")
#assortatywnośc peraosna w sumie to samo
#temp2 = nx.degree_pearson_correlation_coefficient(H)
#print(temp2)
#ppp = list(H.nodes())

#Generate node degree-degree pairs for edges in G.
pair_degree = list(nx.node_degree_xy(H))
 
#avrage neighbor degree - to jest do tego pierwszego
# edit to chyba nit, to dobre jest to: average_degree_connectivity

ggg = dict(nx.average_degree_connectivity(H))

xxx= list()
yyy=list()
# ttt=list(H.edges())
# for i in ttt:
#     xxx.append(i[0])
#     yyy.append(i[1])

for i in pair_degree:
    xxx.append(i[0])
    yyy.append(i[1])

# xxxxxx= list()
# yyyyyy=list()

# for i in range(0,len(ggg)):
#     xxxxxx.append(i.)

# for i in ggg:
#     xxxxxx.append(i[0])
#     yyyyyy.append(i[1])

# fig = plt.figure()
# plt.fig
# fig2 = plt.figure()

#fig = plt.figure()

#fig = plt.subplots(1, 1)
fig=plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Assortativity Pearson')
ax.set_xlabel('node degree')
ax.set_ylabel('node degree')
plt.plot(xxx,yyy,"ro",ms=1)

fig2 = plt.subplots(1, 1)
plt.plot(ggg.keys(),ggg.values(),"ro")
plt.xscale('log')
plt.yscale('log')


# fig3 = plt.subplots(1, 1)
# # m,b = np.polyfit(ggg.keys(), ggg.values(), 1)
temp = list(ggg.keys())

temp2=list(ggg.values())
# fit = np.polyfit(temp,temp2,1)
# fit_fn = np.poly1d(fit) 
# # fit_fn is now a function which takes in x and returns an estimate for y

# #tutaj rzeba zrobić tak by regresja liniowa była dopasowana już do z logarytmowanych dancyh, a nie do liniowych danych(osi) !!!!
# plt.plot(temp,temp2, 'yo', temp, fit_fn(temp), '--k')
# plt.xscale('log')
# plt.yscale('log')

fig4 = plt.subplots(1, 1)
#temp.remove(0)
#temp2.remove(0)
temp3 = np.log(temp)
temp4 = np.log(temp2)
plt.plot(temp3,temp4,"ro")


#tutaj cos się zwaliło z logarytmowaniem małych wartośći
# fig5 = plt.subplots(1, 1)
# #fit = np.polyfit(temp,temp4,1,w=np.sqrt(temp2))

# def func(x, a, b):
#     ttt =a * np.exp(b * x)
#     return ttt

# fit, fit2=sc.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  temp,  temp2)
# print(fit)
# print(fit2)
#fit = np.polyfit(np.log(temp),np.log(temp2),1)
#fit_fn = np.poly1d(fit) 
# # fit_fn is now a function which takes in x and returns an estimate for y

# #tutaj rzeba zrobić tak by regresja liniowa była dopasowana już do z logarytmowanych dancyh, a nie do liniowych danych(osi) !!!!
#plt.plot(temp3,temp4, 'yo', temp3, fit_fn(temp3), '--k')

#plt.plot(temp3,temp4, 'yo', temp3, func(temp3, *fit), '--k')

# temp5 = list()
# for i in temp:
#     temp5.append(func(i,*fit))

# #plt.plot(temp, func(temp, *fit), '--k')
# #plt.plot(temp, temp5, '--k')
# #plt.plot(temp3,temp4, 'yo', temp3, np.log(temp5), '--k')
# plt.plot(temp,temp2, 'yo', temp, temp5, '--k')
# #plt.plot(temp,temp2, 'yo')
# #plt.ylim([1,1000])
# plt.xscale('log')
# plt.yscale('log')
# #plt.show()


#############################
#ten fig działa, regresja liniowa, robię log z x i y, nastenie robię regresję liniową na log(x) log(y)
#rysuję na wykresie log(x) log(y), ponieważ jest to juz przeskalowane logarytmicznie,
#  to nie muszę skalować osi wykresu
###############################

#fig6 = plt.subplots(1, 1)
fig6 = plt.figure()
ax = fig6.add_subplot(111)
ax.set_title('Assortativity Average')
ax.set_xlabel('node degree (k)')
ax.set_ylabel('average degree of nearest neighbors of nodes with degree k')


# fit999 = np.polyfit(np.log(temp),np.log(temp2),1)
# fit_fn999 = np.poly1d(fit) 

logA = np.log(temp)
logB = np.log(temp2)
coefficients = np.polyfit(logA, logB, 1)
print("coefficients  ")
print(coefficients)
polynomial = np.poly1d(coefficients)
print("polynomial   ")
print(polynomial)

ys = polynomial(logA)
#ys = polynomial(temp2)
plt.plot(logA, logB, 'yo', logA, ys, '--k',ms=1)
#plt.plot(temp2, ys)
plt.ylim([0,7])
plt.xlim([0,10])

# slope, intercept, r_value, p_value, std_err = stats.linregress(ggg.keys(), ggg.values())
# print("r-squared:", r_value**2)

# plt.plot(ggg.keys(), ggg.values(), 'o', label='original data')
# plt.plot(ggg.keys(), intercept + slope*ggg.keys(), 'r', label='fitted line')
# plt.legend()
# plt.show()




#plt.plot(uuuu,"ro")

#fig.suptitle('No axes on this figure')  # Add a title so we know which it is

#ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

#data1, data2, data3, data4 = np.random.randn(4, 100)
#fig = plt.subplots(1, 1)
#ax = plt.subplots(1, 1)

#fig.show()
#ax.show()
plt.show()

#nx.draw(H)
#nx.
#plt.show()

#print(temp)
#print(temp2)

#nx.draw(temp)
#plt.show()
print("koniec")

