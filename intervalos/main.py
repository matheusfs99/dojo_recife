# Intervalos (https://dojopuzzles.com/problems/intervalos/)
#
# Este problema foi utilizado em 313 Dojo(s).
#
# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
#
# Exemplo:
#
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
#
# Saída: [100-105], [110-111], [113-115], [150]



def intervals(numbers_list):
    interval = []
    output = []

    for position, i in enumerate(numbers_list):
        if position == 0 or position == 1:
            interval.append(i)
        elif i == interval[-1] + 1:
            if len(interval) > 1:
                interval[-1] = i
            else:
                interval.append(i)
        elif i != interval[-1] + 1:
            output.append(interval)
            interval = []
            interval.append(i)

    if interval:
        output.append(interval)

    return output
