#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    
        yosemite = NationalPark("Yosemite")
        rocky = NationalPark("RMNP")
        lantz = Visitor("Lantz")
        chris = Visitor("Chris")
        matt = Visitor("Matt")
        trip_1 = Trip(matt, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(matt, yosemite, "May 20th", "May 27th")
        trip_3 = Trip(chris, yosemite, "May 5th", "May 9th")
        trip_4 = Trip(lantz, yosemite, "May 5th", "May 9th")
        trip_5 = Trip(chris, rocky, "May 20th", "June 10th")

ipdb.set_trace()
