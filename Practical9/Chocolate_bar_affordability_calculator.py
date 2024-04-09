def affordability(total_money, price_per_piece):
    num_pieces = total_money // price_per_piece
    change = total_money - price_per_piece*num_pieces
    return f"you can afford {num_pieces} piece(s) of chocolate bar. And you still have {change} yuan left."

#Example
total_money = 100
price_per_piece = 7
print(f"Based on the information that you have {total_money} yuan in total and each piece of chocolate bar costs {price_per_piece} yuan, so {affordability(total_money, price_per_piece)}")
#the output is "Based on the information that you have 100 yuan in total and each piece of chocolate bar costs 7 yuan, so you can afford 14 piece(s) of chocolate bar. And you still have 2 yuan left."
