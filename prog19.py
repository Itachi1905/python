letter = "Hey my name is {1} and I am from {0} "
country = "India"
name = "harry"
print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.0999999))

price1 = 49.09999
txt_ = f"For only {price1:.2f} dollars!"
print(txt_)

print(f"{2*30}")