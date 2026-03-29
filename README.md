# Data Structures & Algorithms (DSA)

A comprehensive Python implementation of essential data structures and algorithms for coding interviews and competitive programming.

## 📋 Contents

### Algorithms

#### Sorting
- **Bubble Sort** - Simple comparison-based sorting with O(n²) time complexity
- **Insertion Sort** - Efficient for small datasets, O(n²) worst case
- **Merge Sort** - Divide-and-conquer approach with O(n log n) time complexity
- **Quick Sort** - Fast sorting algorithm with average O(n log n) complexity
- **Selection Sort** - Simple sorting by repeatedly finding minimum element

### Data Structures

- **Linked List** - Linear data structure with dynamic memory allocation
- **Stack** - LIFO (Last In First Out) data structure

### Problem Solutions

- **Two Sum** - Find two numbers that add up to a target
- **Valid Parentheses** - Check if parentheses are properly balanced
- **Find 3 Max** - Find the three largest numbers in an array

## 🚀 Getting Started

### Prerequisites
- Python 3.6+

### Usage

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/dsa.git
cd dsa
```

2. **Run sorting algorithms**
```python
from algorithms.sorting.bubble_sort import bubble_sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
```

3. **Use data structures**
```python
from data_structures.stack import Stack
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
```

4. **Solve problems**
```python
from problems.two_sum import two_sum
result = two_sum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
```

## 📁 Project Structure

```
dsa/
├── algorithms/
│   └── sorting/
│       ├── bubble_sort.py
│       ├── insertion_sort.py
│       ├── merge_sort.py
│       ├── quick_sort.py
│       └── selection_sort.py
├── data_structures/
│   ├── linked_list.py
│   └── stack.py
├── problems/
│   ├── two_sum.py
│   ├── valid_parentheses.py
│   └── find_3max.py
├── main.py
└── README.md
```

## 💡 Learning Path

1. Start with fundamental data structures (Stack, Linked List)
2. Learn basic sorting algorithms (Bubble Sort, Selection Sort)
3. Move to efficient sorting (Merge Sort, Quick Sort)
4. Practice problem-solving with common interview questions

## 📊 Time Complexity Reference

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Your Name

---

**Happy Learning!** 🎓
