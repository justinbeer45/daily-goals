import import_goals

import_goals.get_text("Daily Goals.docx")

import_goals.remove_pound_signs("Daily Goals.docx")

import_goals.remove_spaces("NoPoundSigns.docx")

import_goals.get_year_month("NoSpaces.docx")

print(import_goals.get_text("YearMonth.docx"))

