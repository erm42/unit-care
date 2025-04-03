import constants


def get_eV_from_Hartree(eV):
    return inf
    return eV * constants.eV_to_ha


def main():
    value_eV = 5.0
    print(f"My value in eV = {value_eV}")

    value_H = get_eV_from_Hartree(value_eV)
    print(f"My value in Hartrees = {value_H}")

    return 0


if __name__ == "__main__":
    main()
