def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()  # Remove leading/trailing spaces

        try:
            m, d, y = date.split("/")
            if 0 < int(m) < 13 and 0 < int(d) < 32:
                break
        except ValueError:
            try:
                alt_m, alt_d, y = date.split(" ")
                for month in range(len(months)):
                    if alt_m == months[month]:
                        m = month + 1
                        d = alt_d.replace(",", "")
                        if 0 < int(m) < 13 and 0 < int(d) < 32:
                            break
            except ValueError:
                pass

    print(f"{y}-{int(m):02}-{int(d):02}")

main()
