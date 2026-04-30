# currency converter (simple version)

def convert_to_usd(cop, pen, brl):
    rate_cop = 0.000249
    rate_pen = 0.2814
    rate_brl = 0.1799

    usd_cop = cop * rate_cop
    usd_pen = pen * rate_pen
    usd_brl = brl * rate_brl

    total = usd_cop + usd_pen + usd_brl
    return usd_cop, usd_pen, usd_brl, total


def main():
    try:
        cop = float(input("Enter Colombian Pesos (COP): "))
        pen = float(input("Enter Peruvian Soles (PEN): "))
        brl = float(input("Enter Brazilian Reais (BRL): "))
    except:
        print("Invalid input")
        return

    usd_cop, usd_pen, usd_brl, total = convert_to_usd(cop, pen, brl)

    print("\n--- Result ---")
    print("COP to USD:", round(usd_cop, 2))
    print("PEN to USD:", round(usd_pen, 2))
    print("BRL to USD:", round(usd_brl, 2))
    print("Total USD:", round(total, 2))


main()
