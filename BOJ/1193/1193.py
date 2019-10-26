# Get one digit
i = int(input())

# Estimate line index
abstract = -0.5 + (2*i + 0.25)**0.5
line = -1

if abstract == abstract // 1:
    line = int(abstract)
else:
    line = int(abstract) + 1

linesum = line + 1
# Estimate distance
distance = i - (line - 1) * line // 2

# Make fountain
up, dw = distance, linesum - distance

if line % 2 == 0:
    dw, up = up, dw

# Print
print('{}/{}'.format(dw, up))
