"""drop_drop"""
def main():
    """first"""
    grade1 = float(input())
    if grade1 < 1.00:
        print("I'm so sad.")
    elif grade1 < 2.00:
        grade2 = 4 - grade1
        print("%.2f" %grade2)
    else:
        print("I'm so happy.")
main()
