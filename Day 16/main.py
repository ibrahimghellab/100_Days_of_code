import prettytable

table= prettytable.PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name","Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

print(table)