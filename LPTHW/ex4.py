#coding=utf-8

cars=100#给cars赋值100
space_in_a_car=4.0#给space_in_a_car赋值
drivers=30#给drivers赋值
passengers=90#给passengers赋值
cars_not_driven= cars - drivers#cars_not_drivens是用cars减drivers获得的
cars_driven=drivers#cars_driven等于drivers的值
carpool_capacity= cars_driven * space_in_a_car#carpool_capacity的值是通过cars_driven乘以space_in_a_car得出的
average_passengers_per_car= passengers / cars_driven#average_passengers_per_car的值是通过passengers除以cars_driven得出的


print("There are ",cars,"cars available.")#打印cars的值
print("There only ",drivers,"drives available.")#打印drivers的值
print("There will be",cars_not_driven,"empty cars today.")#打印cars_not_driven的值
print("We can transport",carpool_capacity,"people today.")#打印car_pool_capacity的值
print("We have",passengers,"to carpool today.")#打印passengers的值
print("We need to put about",average_passengers_per_car,"in each car.")#打印average_passengers_per_car的值