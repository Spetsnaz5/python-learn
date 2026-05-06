for x in range(10):
    try:
        if x == 5:
            raise ValueError("An error occurred at x = 5")
        elif x == 8:
            #pass
            break
        print(f"Processing {x}")
    except ValueError as e:
        print(f"Caught an error: {e}")
    finally:
        print(f"Cleaning up after processing {x}\n")