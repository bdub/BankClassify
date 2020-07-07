from BankClassify import BankClassify

#bc = BankClassify()
bc = BankClassify(data="STG_AllData.csv")

#bc.add_data("85561768_20205411_0903.csv", "lloyds")
#bc.add_data("data/STG_[112-879 099143271] Visa Freedom_2017.07.01-2020.06.30.csv", "stgeorge")
bc.add_data("data/STG_snippet_2020_04-03.csv", "stgeorge")
