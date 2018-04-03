# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.ai.HolidayGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.ai.HolidayDates import *
Month = Enum('JANUARY, FEBRUARY, MARCH, APRIL,               MAY, JUNE, JULY, AUGUST, SEPTEMBER,               OCTOBER, NOVEMBER, DECEMBER', 1)
Day = Enum('MONDAY, TUESDAY, WEDNESDAY, THURSDAY,             FRIDAY, SATURDAY, SUNDAY')
holidays = {PiratesGlobals.DOUBLEGOLDHOLIDAY: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                    (
                                     2008, Month.SEPTEMBER, 13, 12, 0, 0), (2008, Month.SEPTEMBER, 13, 15, 0, 0)]), 
   PiratesGlobals.DOUBLEGOLDHOLIDAYPAID: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                        (
                                         2008, Month.SEPTEMBER, 14, 12, 0, 0), (2008, Month.SEPTEMBER, 14, 15, 0, 0)]), 
   PiratesGlobals.DOUBLEXPHOLIDAY: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                  (
                                   2008, Month.SEPTEMBER, 27, 12, 0, 0), (2008, Month.SEPTEMBER, 27, 15, 0, 0)]), 
   PiratesGlobals.DOUBLEXPHOLIDAYPAID: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                      (
                                       2008, Month.SEPTEMBER, 28, 12, 0, 0), (2008, Month.SEPTEMBER, 28, 15, 0, 0)]), 
   PiratesGlobals.FREEHATWEEK: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                              (
                               2008, Month.FEBRUARY, 25, 0, 0, 0), (2008, Month.MARCH, 2, 0, 0, 0)]), 
   PiratesGlobals.SAINTPATRICKSDAY: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                   (
                                    2008, Month.MARCH, 14, 0, 0, 0), (2008, Month.MARCH, 18, 0, 0, 0)]), 
   PiratesGlobals.MOTHERSDAY: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                             (
                              2008, Month.MAY, 10, 0, 0, 0), (2008, Month.MAY, 12, 0, 0, 0)]), 
   PiratesGlobals.FATHERSDAY: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                             (
                              2008, Month.JUNE, 13, 0, 0, 0), (2008, Month.JUNE, 16, 0, 0, 0)]), 
   PiratesGlobals.FOURTHOFJULY: HolidayDates(HolidayDates.TYPE_YEARLY, [
                               (
                                Month.JULY, 3, 18, 0, 0), (Month.JULY, 7, 0, 0, 0)]), 
   PiratesGlobals.HALFOFFCUSTOMIZATION: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                       (
                                        2008, Month.AUGUST, 14, 0, 0, 0), (2008, Month.AUGUST, 18, 12, 0, 0)]), 
   PiratesGlobals.ALLACCESSWEEKEND: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                   (
                                    2008, Month.AUGUST, 14, 0, 0, 0), (2008, Month.AUGUST, 18, 12, 0, 0)]), 
   PiratesGlobals.HALLOWEEN: HolidayDates(HolidayDates.TYPE_YEARLY, [
                            (
                             Month.OCTOBER, 31, 3, 0, 0), (Month.NOVEMBER, 3, 0, 0, 0)]), 
   PiratesGlobals.JOLLYROGERCURSE: HolidayDates(HolidayDates.TYPE_CUSTOM, [
                                  (
                                   2008, Month.OCTOBER, 31, 12, 0, 0), (2008, Month.OCTOBER, 31, 12, 30, 0), (2008, Month.OCTOBER, 31, 17, 0, 0), (2008, Month.OCTOBER, 31, 17, 30, 0), (2008, Month.OCTOBER, 31, 20, 0, 0), (2008, Month.OCTOBER, 31, 20, 30, 0), (2008, Month.NOVEMBER, 1, 12, 0, 0), (2008, Month.NOVEMBER, 1, 12, 30, 0), (2008, Month.NOVEMBER, 1, 16, 0, 0), (2008, Month.NOVEMBER, 1, 16, 30, 0), (2008, Month.NOVEMBER, 1, 21, 0, 0), (2008, Month.NOVEMBER, 1, 21, 30, 0), (2008, Month.NOVEMBER, 2, 13, 0, 0), (2008, Month.NOVEMBER, 2, 13, 30, 0), (2008, Month.NOVEMBER, 2, 16, 0, 0), (2008, Month.NOVEMBER, 2, 16, 30, 0), (2008, Month.NOVEMBER, 2, 19, 0, 0), (2008, Month.NOVEMBER, 2, 19, 30, 0)])}
holidaysEnglish = {}
holidaysJapanese = {}
holidaysGerman = {}
holidaysFrench = {}

def getHolidayDates(holidayId):
    return holidays.get(holidayId)


holidayMessages = {PiratesGlobals.DOUBLEGOLDHOLIDAY: (PLocalizer.DoubleGoldStart, PLocalizer.DoubleGoldStartChat, PLocalizer.DoubleGoldEnd, PLocalizer.DoubleGoldEnd, PLocalizer.CHAT_STATUS_DOUBLEGOLD, 'admin'), PiratesGlobals.DOUBLEGOLDHOLIDAYPAID: (PLocalizer.DoubleGoldFullStart, PLocalizer.DoubleGoldFullStartChat, PLocalizer.DoubleGoldFullEnd, PLocalizer.DoubleGoldFullEnd, PLocalizer.CHAT_STATUS_DOUBLEGOLD_PAID, 'admin'), PiratesGlobals.DOUBLEXPHOLIDAY: (PLocalizer.DoubleXPStart, PLocalizer.DoubleXPStartChat, PLocalizer.DoubleXPEnd, PLocalizer.DoubleXPEnd, PLocalizer.CHAT_STATUS_DOUBLEXP, 'admin'), PiratesGlobals.DOUBLEXPHOLIDAYPAID: (PLocalizer.DoubleXPFullStart, PLocalizer.DoubleXPFullStartChat, PLocalizer.DoubleXPFullEnd, PLocalizer.DoubleXPFullEnd, PLocalizer.CHAT_STATUS_DOUBLEXP_PAID, 'admin'), PiratesGlobals.BLACKJACKFRIDAY: (PLocalizer.BlackJackFridayStart, PLocalizer.BlackJackFridayStartChat, PLocalizer.BlackJackFridayEnd, PLocalizer.BlackJackFridayEndChat, PLocalizer.CHAT_STATUS_BLACKJACK_FRIDAY, 'friends'), PiratesGlobals.FREEHATWEEK: (PLocalizer.FreeHatStartUnlimited, PLocalizer.FreeHatStartUnlimitedChat, None, None, None, 'admin'), PiratesGlobals.SAINTPATRICKSDAY: (PLocalizer.StPatricksStartUnlimited, PLocalizer.StPatricksStartUnlimitedChat, None, None, None, 'admin'), PiratesGlobals.MOTHERSDAY: (PLocalizer.MothersDayStartUnlimited, PLocalizer.MothersDayStartUnlimitedChat, None, None, PLocalizer.CHAT_STATUS_MOTHERS_DAY_PAID, 'tattoo'), PiratesGlobals.FATHERSDAY: (PLocalizer.FathersDayStart, PLocalizer.FathersDayStartChat, None, None, PLocalizer.CHAT_STATUS_FATHERS_DAY, 'admin'), PiratesGlobals.FOURTHOFJULY: (PLocalizer.FourthOfJulyStart, PLocalizer.FourthOfJulyStartChat, None, None, PLocalizer.CHAT_STATUS_FOURTHOFJULY, 'admin'), PiratesGlobals.HALFOFFCUSTOMIZATION: (PLocalizer.HalfOffCustomizationUnlimited, PLocalizer.HalfOffCustomizationUnlimited, PLocalizer.HalfOffCustomizationEnd, PLocalizer.HalfOffCustomizationEnd, PLocalizer.HalfOffCustomizationStatus, 'admin'), PiratesGlobals.ALLACCESSWEEKEND: (PLocalizer.UnlimitedAccessEventBasic, PLocalizer.UnlimitedAccessEventBasic, None, None, PLocalizer.AllAccessHolidayStart, 'admin'), PiratesGlobals.HALLOWEEN: (PLocalizer.HalloweenStart, PLocalizer.HalloweenStartChat, PLocalizer.HalloweenEnd, PLocalizer.HalloweenEnd, PLocalizer.CHAT_STATUS_HALLOWEEN, 'admin'), PiratesGlobals.JOLLYROGERCURSE: (None, None, None, None, PLocalizer.CHAT_STATUS_JOLLYROGERCURSE, 'admin')}

def getHolidayStartMsg(holidayId):
    return holidayMessages.get(holidayId)[0]


def getHolidayStartChatMsg(holidayId):
    return holidayMessages.get(holidayId)[1]


def getHolidayEndMsg(holidayId):
    return holidayMessages.get(holidayId)[2]


def getHolidayEndChatMsg(holidayId):
    return holidayMessages.get(holidayId)[3]


def getHolidayStatusMsg(holidayId):
    return holidayMessages.get(holidayId)[4]


def getHolidayIcon(holidayId):
    return holidayMessages.get(holidayId)[5]
# okay decompiling .\pirates\ai\HolidayGlobals.pyc
