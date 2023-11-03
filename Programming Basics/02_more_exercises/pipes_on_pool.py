volume_pool = int(input())
p1_flow_rate = int(input())
p2_flow_rate = int(input())
hours = float(input())

water_added = (p1_flow_rate + p2_flow_rate) * hours
p1_total_amount = (p1_flow_rate * hours) / water_added * 100
p2_total_amount = (p2_flow_rate * hours) / water_added * 100
water_level = water_added / volume_pool * 100

if water_added <= volume_pool:
    print(f'The pool is {water_level}% full. Pipe 1: {p1_total_amount:.2f}%. Pipe 2: {p2_total_amount:.2f}%.')
elif water_added > volume_pool:
    print(f'For {hours} hours the pool overflows with {water_added - volume_pool:.2f} liters.')
