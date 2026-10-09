
from typing import List, Union


def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    return unique_numbers


def find_average(numbers: List[int]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def multiply_by_scalar(numbers: List[int], scalar: Union[int, float]) -> List[Union[int, float]]:
    return [num * scalar for num in numbers]


def main():
    print("=" * 60)
    print("           ASSIGNMENT 02 - QUESTION # 01 SOLUTION           ")
    print("=" * 60)

    # Sample input list of integers
    sample_list = [10, 20, 10, 30, 40, 20, 50, 30, 60]
    scalar_multiplier = 3

    print(f"\nOriginal List: {sample_list}")
    print(f"Scalar Value:  {scalar_multiplier}\n")

    # 1. Test remove_duplicates
    unique_result = remove_duplicates(sample_list)
    print(f"1. remove_duplicates(sample_list):")
    print(f"   -> Result: {unique_result}")

    # 2. Test find_average
    average_result = find_average(sample_list)
    print(f"\n2. find_average(sample_list):")
    print(f"   -> Sum = {sum(sample_list)}, Count = {len(sample_list)}")
    print(f"   -> Average Result: {average_result:.2f}")

    # 3. Test multiply_by_scalar
    scaled_result = multiply_by_scalar(sample_list, scalar_multiplier)
    print(f"\n3. multiply_by_scalar(sample_list, {scalar_multiplier}):")
    print(f"   -> Result: {scaled_result}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
