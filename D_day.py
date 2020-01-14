from datetime import date

class Dday:

    def countDays(self, year, month, day):
        self.result = date(year, month, day)
        return self.result

    def countHoli(self, year, month, day):
        pass

    def countWeekend(self, year, month, day):
        self.result = date(year, month, day).weekday()
        return self.result

startYear = int(input('시작일의 연도를 입력하세요: '))
startMonth = int(input('시작일의 월을 입력하세요: '))
startDay = int(input('시작일의 일을 입력하세요: '))

endYear = int(input('종료일의 연도를 입력하세요: '))
endMonth = int(input('종료일의 월을 입력하세요: '))
endDay = int(input('종료일의 일을 입력하세요: '))

a = Dday()

totalDays = a.countDays(endYear, endMonth, endDay) - a.countDays(startYear, startMonth, startDay)

print('총 기간은 %s입니다.'%totalDays)
