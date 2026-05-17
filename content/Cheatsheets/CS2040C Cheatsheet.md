
### Back To C++! 
```c++
using namespace std;

cout << "Hello World";
cin >> bigint;
```
#### Delete and Pointers
```c++
double *studentmark;
studentmark = new double;

*studentmark = 101.0;
double x = 120;
studentmark = &x; // &x returns the location of x for studentmark to point to

delete studentmark;
```
#### Dynamic Arrays

```c++
double *studentmarks;
studentmarks = new double [num];
delete [] studentmarks
```

#### Pass By Reference
```c++
void swap(int &a, int &b){
	int temp = p;
	a = b;
	b = temp;
}

int a=1,b=2;
swap(a,b);
```

#### Function Overloading
```c++
void add(){

}
int add(int a, int b){

}
int add(int a, int b, int c){

}
```
This code is valid. The function can be of the same name but the function type must be different or the number of function parameters must be different



There are three types of potential calculations for time complexity.
- Recursive
	- Form a recursive relation.
	- Solve for how many it is ran / write down to see a picture
	- Find the complexity
```c++
void f(int n) {
	if (n<10) return 0;
	return f(7*n/9);
}
```
- Normal
	- No issue here, just count the number of for-loops and consider the conditions
- Strange for-loops
	- Attempt to consider the worst case scenario and take the slowest growth pattern
```c++
int f(int n) {
	for (int i = 0; i < n; i*=2)
		for (int j = i; j < n; j++)
			i+=1;
}
```


#### Big O
• Pick the highest degree/order term
• Stripped all the coefficients
![[Pasted image 20250129173537.png|500]]

Loops
• cost = (# iterations)x(max cost of one iteration)

**For binary search:**

![[Pasted image 20250129173708.png]]




If it is simple loops, just count the number of for loops and consider the conditions within them
If it is recursive, write a recursive relation like $T(N)=T(N/2) + O(1)$


**Lazy evaluation** -> Only calculate when I need it




#### 1D Peak Finding O(logN)
```
FindPeak(A, n)
	mid = n/2
	if A[mid] is a peak then return mid
	else if A[mid+1] > A[mid] then
		Search for peak in right half.
	else if A[mid-1] > A[mid] then
		Search for peak in left half
```

##### 2D Peak Finding
![[Pasted image 20250207115711.png]]
Calculate in the middle
9 10 12

That is not the peak. 
Move to the right

It will find a LOCAL 2D Peak.



![[Pasted image 20250208133729.png]]
ADT is the 'framework'

Interface: How others communicate with it
Implementation > Inner workings

### Stack
**Interface**
`pop()`
`push()`
`empty()`

**Implementation**
First In, Last Out
### Queue
**Interface**
`enqueue` -> add element to front of queue
`dequeue` -> remove element from end of queue


First In, First Out
### List
Either Side In, Either Side Out


![[Pasted image 20250129171024.png]]

A basic datastructure that to deal with variable data sizes. 
During runtime, size of the data will change (increase or decrease). Using malloc, calloc is very suboptimal. 


**<LinkedList.h>**
```c++
#pragma once
#ifndef LINKED_LIST_H
#define LINKED_LIST_H

  

#include <initializer_list>
#include <string>

  
struct Node{
	int element;
	Node *next;

	Node(int element) : element{ element }, next{ nullptr } {}
	Node(int element, Node* next) : element{ element }, next{ next } {}
}

class List{
private:
	size_t m_size;
	Node *m_head;

class List {
  private: size_t m_size;
  Node * m_head;

  public:
    // Constructs an empty container
    List(): m_size { 0 },m_head { nullptr } {}

  // Constructs the container with the contents of the initializer list
	  List(std::initializer_list < int > init_list){
	  m_size = 0;
	  m_head = nullptr;
    auto it = init_list.end();
    while (--it != init_list.begin()) {
      push_head( * it);
    }
    push_head( * it);
  }

  // Returns the value at head
  int head();

  // Checks whether the container is empty
  bool empty() const;

  // Returns the number of elements
  size_t size() const;

  // Inserts an element to the head
  void push_head(int element);

  // Removes the head element and returns its value
  int pop_head();

  // Checks whether the container contains the specified element
  bool contains(int element) const;

  // Converts the container to std::string
  std::string to_string() const;
};
#endif
```


`<LinkedList.cpp>` implementation
```c++
#include "LinkedList.h"

// copy the following code to coursemology without the above line of "#include "LinkedList.h""

// Returns the value at head

#include <stdexcept>

int List::head() {
  // Works.
  if (m_head == nullptr) {
    throw std::out_of_range("List is empty");
  }
  return m_head -> element;
}

// Checks whether the container is empty
bool List::empty() const {
  // Works
  return (m_size == 0);
}

// Returns the number of elements
size_t List::size() const {
  // Works
  return m_size;
}

// Inserts an element to the head
void List::push_head(int element) {
  // Works
  Node * newnode = new Node(element, m_head);
  m_head = newnode;
  m_size++;
}

// Removes the head element
int List::pop_head() {
  // TODO: Implement this method
  if (m_size == 0 || m_head == nullptr) {
    throw std::out_of_range("List is empty");
  }
  Node * temp = m_head;
  int value = temp -> element;
  m_head = m_head -> next;

  delete temp;
  m_size--;
  return value;
}

// Checks whether the container contains the specified element
bool List::contains(int element) const {
  // Works
  if (m_size == 0 || m_head == nullptr) {
    return false;
  }

  Node * temp = m_head;
  while (temp != nullptr) {
    if (temp -> element == element) {
      return true;
    }
    temp = temp -> next;
  }
  return false;
}

// Returns a std::string equivalent of the container
std::string List::to_string() const {
  // Works
  std::string str = "{";
  Node * temp = m_head;
  while (temp != nullptr) {
    str += std::to_string(temp -> element);
    if (temp -> next != nullptr) {
      str += ", ";
    }
    temp = temp -> next;
  }

  str += "}";
  return str;
}
```


Single inheritance 
A -> B -> C (single inheritance through multiple levels, NOT multiple inheritance)

**Multiple inheritance:** This occurs when a single class directly inherits from **two or more** distinct parent classes.
- Example: `class A : public B, public C`.
#### OOP
In C:
```c
typedef struct {
	int acc_num;
	int acc_total;
}BankAccount;
```
There are issues due to access. acc_total can be accessed and modified.

In c++:
```c++
class BankAccount{
private:
	int _acc_total;
	int _acc_num;
public:
	int withdraw(int acc_num, int amount){
		if(acc_num == _acc_num){
			// allow access
		}
	}
	int deposit(int acc_num, int amount); // declare but have not programmed
}


// Declare how the function works outside
int BankAccount::deposit(int acc_num, int amount){
	if(acc_num == _acc_num){
		// note how _acc_num can be accessed here.
	}
}



BankAccount AlanAcc;
AlanAcc._acc_total = 1000; // This is invalid
```


#### Constructors
```c++
class BankAccount{
private:
	int _acc_total;
	int _acc_num;
public:
	BankAccount() : _acc_total {0}, _acc_num {NULL} {}  // constructor option 1

	BankAccount(){
		_acc_total = 0;
		_acc_num = NULL;
	}
	// option 2

	// option 3
	BankAccount();
}

// option 3
BankAccount::BankAccount(){
	_acc_total = 0;
	_acc_num = NULL;
}
```

#### friend
Sometimes you just need a friend.
Classes have private variables. Sometimes it needs to be accessed by other classes. Use the keyword `friend`
```c++
class ListNode{
private:
	int element;
	ListNode* next;
public:
	ListNode(int);
friend class List;
}
```

#### destructor
The Destructor will be called when an instance of the class is deleted
```c++
class List{
private:
	int size;
	ListNode* head;
public:
	List(); // constructor
	~List(); // destructor
	void removeHead();
};

List::~List(){
	while(size != 0){
		removeHead();
	}
}
```


### Inheritance and Polymorphing
```c++
class betterStack: public Stack{
public:
	void push(int);
	int pop();
};
```
The subclass `betterStack` has all the functionality of `Stack` but the same named functions will OVERRIDE

Child class' functions cannot access 'private' of the parents function. To allow this to happen, use `protected`

```c++
class Stack{
protected:
	List _ll;
}
```




### Virtual and Dynamic Dispatch

A virtual function is a function declared in a base class that is intended to be redefined (overridden) in derived classes, enabling **dynamic dispatch**. When you call a virtual function through a pointer or reference to the base class, the version of the function that executes is determined at runtime based on the actual type of the object, rather than the type of the pointer or reference.

We talked about how inheritance can override functions like so
```c++
int BeeBooStack<int>::pop() {
	cout << "Boo" << endl;
	return Stack::pop();
}
```

But this is only the case when `BeeBooStack bbStack` is in use. If we go back to using `Food`, this function is not overridden.

But what if:
```c++
Stack *s;
BeeBooStack bbsi;
s = &bbsi;
s->push(10);
```
Which push will be called?
It calls Stack::push()


`virtual` helps to avoid this issue
```c++
class Animal {
public:
	virtual void talk()
	{ cout << "*Nothing*" << endl; }
};
class Dog :public Animal {
public:
	virtual void talk()
	{ cout << "Woof" << endl; }
};
class Cat :public Animal {
public:
	virtual void talk()
	{ cout << "Meow" << endl; }
};


Animal *dolly = new Dog();
Animal *orange = new Cat();
dolly->talk(); // This outputs Woof
orange->talk(); // This outputs meow
```
TLDR: `virtual` allows you to use pointers from the parent's class to store objects of child classes.


An example:
```c++
#include <iostream>
#include <fstream>
#include <string>

class Logger {
public:
    virtual ~Logger() = default;
    virtual void logMessage(const std::string &message) const = 0; // pure virtual
};

class ConsoleLogger : public Logger {
public:
    void logMessage(const std::string &message) const override {
        std::cout << "[Console] " << message << std::endl;
    }
};

class FileLogger : public Logger {
private:
    std::string filename;
public:
    FileLogger(const std::string &fname) : filename(fname) {}
    void logMessage(const std::string &message) const override {
        std::ofstream ofs(filename, std::ofstream::app);
        ofs << "[File] " << message << std::endl;
    }
};

int main() {
    Logger *logger = new ConsoleLogger();
    logger->logMessage("Hello from console logger!");

    // Switch to a file logger without changing other code
    delete logger;
    logger = new FileLogger("log.txt");
    logger->logMessage("Hello from file logger!");

    delete logger;
    return 0;
}
```


```c++
class Food{
private:
	string _name;
	int calories;
public:
	Food() { name = ""; calories = 0;};
	Food(string name, int cal){
		_name = name;
		calories = cal;
	};

	bool operator>(const Food&);

	friend ostream &operator<<(ostream& out, const Food&f);
	// friend gives operator function access to private members
};

bool Food::operator>(const Food& f){
	return calories > f.calories;
}

ostream &operator<<(ostream &out, const Food &f){
	out << "Food: " << f._name << ", Calories: " << f.calories;
	return out;
}
```

- understand quicksort more.
- write code for the rest


Let’s Say We Want to Sort the class FOOD
```c++
class Food{
private:
	string _name;
	int calories;
public:
	Food() { name = ""; calories = 0;};
	Food(string name, int cal){
		_name = name;
		calories = cal;
	};

	bool operator>(const Food&);

	friend ostream &operator<<(ostream& out, const Food&f);
	// friend gives operator function access to private members
};

bool Food::operator>(const Food& f){
	return calories > f.calories;
}

ostream &operator<<(ostream &out, const Food &f){
	out << "Food: " << f._name << ", Calories: " << f.calories;
	return out;
}
```



| Sorting Algorithm | Description                                                                                                                                                                                                           | Stability |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Bubble Sort       | Swapping adjacent elements                                                                                                                                                                                            | Stable    |
| Insertion Sort    | Compare and shift elements to insert itself in between.                                                                                                                                                               | Stable    |
| Selection Sort    | Selecting smallest element over A[i:n] and swap. Selection Sort **swaps elements that are far apart**, not just adjacent ones.                                                                                        | Unstable  |
| Merge Sort        | Dividing the array into two, merging it back together while keeping it sorted. Merging back and keeping it sorted is done by having two queues and merging into one array by comparing the top element of each queue. | Stable    |
| Quick Sort        | Similar to merge sort. Instead of merging, we use partitioining.                                                                                                                                                      | Unstable  |
| Count Sort        | Form a counting array using the index as the number and the count as the number of elements already in the sorted list.                                                                                               | Unstable  |



| Sorting Algorithm | Best Time | Worst Time | When to Use                                                                                         |
| ----------------- | --------- | ---------- | --------------------------------------------------------------------------------------------------- |
| Bubble Sort       | O(N)      | O(N^2)     |                                                                                                     |
| Insertion Sort    | O(N)      | O(N^2)     | Insertion sort is fast when<br>array is almost sorted<br>array is small<br>use when sample n < 1000 |
| Selection Sort    | O(N^2)    | O(N^2)     |                                                                                                     |
| Merge Sort        | O(nlogN)  | O(nlogN)   |                                                                                                     |
| Quick Sort        | O(nlogN)  | N^2        | Don't use when almost sorted. Becomes N^2                                                           |
| Count Sort        | O(N+M)    | O(N+M)     | When max number is small                                                                            |

### Bubble Sort
- Repeatedly swap adjacent values. For ascending sorting, high values 'bubble up'
```c++
template < class T > void bubble_sort(T a[], int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (a[j] > a[j + 1]) {
        swap(a[j], a[j + 1]);
      }
    }
  }
}
```
### Insertion Sort
- Iteratively inserting each element in the unsorted section of the list into the sorted section
```c++
template <typename T>
void insertion_sort(T arr[], int n) {
    for (int i = 1; i < n; i++) { // O(N)
        T temp = arr[i]; // temp is the item to be inserted
        int j = i - 1;
        while (j >= 0 && arr[j] > temp) { // can be fast or slow
            arr[j + 1] = arr[j]; // make a place for temp
            j--;
        }
        arr[j + 1] = temp; // this is the insertion point
    }
}
```

### Selection Sort
- Repeatedly select the smallest/largest element from the unsorted portion and swapping it with the first unsorted element
```c++
template <class T> void selection_sort(T arr[], int n){
	for(int i =0;i<n;i++){
		int min_index = i;

		for(int j=i+1; j<n;j++){
			if(arr[j] < arr[min_index]){
				min_index = j;
			}
		}
	
		swap(arr[i], arr[min_index]);
	}
}
```
### Merge Sort
- Uses divide and conquer. Stable. Efficient. Recursively divide the array into subarrays, sorting those subarrays and then merge them back
- Read the code. It makes sense

```cpp
void merge(int a[], int low, int mid, int high) {
  // subarray1 = a[low..mid], subarray2 = a[mid+1..high], both sorted
  int N = high - low + 1;
  int b[N];
  int left = low, right = mid + 1, bIdx = 0;
  while (left <= mid && right <= high)  // the merging
    b[bIdx++] = (a[left] <= a[right]) ? a[left++] : a[right++];
  while (left <= mid) b[bIdx++] = a[left++];      // leftover, if any
  while (right <= high) b[bIdx++] = a[right++];   // leftover, if any
  for (int k = 0; k < N; k++) a[low + k] = b[k];  // copy back
}
void MergeSort(int a[], int low, int high) {
  // the array to be sorted is a[low..high]
  if (low < high) {  // base case: low >= high (0 or 1 item)
    int mid = (low + high) / 2;
    MergeSort(a, low, mid);       // divide into two halves
    MergeSort(a, mid + 1, high);  // then recursively sort them
    merge(a, low, mid, high);     // conquer: the merge routine
  }
}

int main() {
  int arr[] = {3, 1, 20, 2, -1, -5, 100};
  int n = 7;
  MergeSort(arr, 0, n - 1);
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";
}
```
### Quick Sort
- Uses divide and conquer. Picks an element as a pivot and partitions the given array around the pivot.
- Has a sub-algorithm for dealing with duplicates (packDuplicates) where the Quick Sort's partitioning step groups identical values together
	- This makes it more efficient for arrays with repeated elements.

- Partitioning has four steps
	- Choosing the pivot
	- Finding all elements smaller than the pivot 
	- Finding all elements larger than the pivot
	- Moving the elements smaller than the pivot to one side and the larger to one side
- This can be done using the double pointer method
	- Choose the first number as the partition
	- Have two pointers, one moving to the left (from the end) (`right_ptr`) and one to the right (from the start) (`left_ptr`)
		- `left_ptr` will stop when it finds an element higher than the first element
		- `right_ptr` will stop when it finds an element lower than the first element
		- Then it will swap
		- When `left_ptr` == `right_ptr` -> swap first element with position `left_ptr - 1`
![[Pasted image 20250207153436.png|300]]![[Pasted image 20250207153658.png|300]]
**Do not use when nearly sorted/sorted**
If QuickSort is implemented with a **deterministic pivot selection strategy**, such as always picking:

- **The first element** as the pivot.
- **The last element** as the pivot.
- **The smallest or largest element** as the pivot.

then **already sorted or nearly sorted data** leads to **unbalanced partitions**, causing worst-case behavior.

```c++
int partition(int arr[], int i, int j) {
  int p = arr[i];                     // p is the pivot
  int m = i;                          // S1 and S2 are initially empty
  for (int k = i + 1; k <= j; k++) {  // explore the unknown region
    if (arr[k] < p) {
      m++;
      swap(arr[k], arr[m]);  // C++ STL algorithm std::swap
    }  // notice that we do nothing in case 1: a[k] >= p
  }
  swap(arr[i], arr[m]);  // final step, swap pivot with arr[m]
  return m;              // return the index of pivot, to be used by Quick Sort
}
void quickSort(int arr[], int low, int high) {
  if (low < high) {
    int pivotIdx = partition(arr, low, high);  // O(N)
    // a[low..high] ~> a[low..pivotIdx–1], pivot, a[pivotIdx+1..high]
    quickSort(arr, low, pivotIdx - 1);  // recursively sort left subarray
    // a[pivotIdx] = pivot is already sorted after partition
    quickSort(arr, pivotIdx + 1, high);  // then sort right subarray
  }
}

int main() {
  int arr[] = {3, 1, 20, 2, -1, -5, 100};
  int n = 7;
  quickSort(arr, 0, n - 1);
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";
}
```


### Count Sort
- non-comparison-based sorting algorithm. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted




```c++
ostream& operator<<(ostream&os, const food& f){

}
```

### C++ Templates
```c++
void swap(T& s1, T& s2)
```


![[Pasted image 20250207203909.png]]


AVL Tree with successor and predecessor functions

When working with AVL trees, we often need to find:

- **Successor**: The smallest key that is **larger** than the given key.
- **Predecessor**: The largest key that is **smaller** than the given key.****

**Order statistics**
We can find the rank of the node using the weight of the node's subtree. This is log(n). **Importantly, this solves the issue of using rank for order statistics, which cost O(n) to update.**
- If **X has no children**, `Size(X) = 1`
- If **X has only a left child**, `Size(X) = 1 + Size(left_subtree)`
- If **X has only a right child**, `Size(X) = 1 + Size(right_subtree)`
- If **X has both children**, `Size(X) = 1 + Size(left_subtree) + Size(right_subtree)`

The **rank** of a node is its position in an **in-order traversal**.

- **O(log n)** per rank lookup (similar to AVL search).
- **O(log n)** per insertion/deletion (must update `size` field).

**EXAMPLE:**
```
        50 (Size=7)
       /       \
    30 (3)     70 (3)
   /   \       /    \
 10(1) 40(1) 60(1)  80(1)

```
#### **Finding the Rank of 60**

1. Start at **50**:
    - 60 is **greater than 50**, so move right.
    - **Add** `Size(left_subtree of 50) + 1` → `3 + 1 = 4`
2. Now at **70**:
    - 60 is **less than 70**, so move left.
    - Rank remains `4`
3. Now at **60**
    - 60 is found!
    - **Final Rank = 4 + 1 = 5**
📌 **Rank of 60 is 5.**




Use an AVL Tree with order statistics. (Or remember the weight of each subtree to compute the rank of every node)
To compute the number of sales = rank b – rank a + 1
Time complexity for each operation = O(log n)

A **binary search tree (BST)** does **not guarantee** O(log⁡N)O(\log N)O(logN) search time unless it is **balanced**.

![[Pasted image 20250226175613.png]]
#### Traversal
- In Order
	- Left -> Root -> Right
	- In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.
- Pre Order
	- Root -> Left -> Right
	- Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree
- Post Order
	- Left -> Right -> Root
	- Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree
- Level
	- By height
	- Use Queue
```
queue q;
add root to q;
while(q is not empty){
	dequeue q, assign as x
	print x
	push the children of x into the queue
}
```

![[Pasted image 20250226162634.png|200]]![[Pasted image 20250226162658.png|200]]![[Pasted image 20250226162708.png|200]]
![[Pasted image 20250226162714.png|200]]



BST - Binary Search Tree.
Left child contain values that are less than parent node. Right child contain values that are more than parent node. Insertion, searching and deletion are efficient - O(logN) when implemented properly
![[Pasted image 20250207155236.png|100]]


### Deleting Nodes
Deleting nodes can occur in three manners.
- Deleting a node with no child
	- No concerns here, simply delete without needing extra details. Simply delete yourself
- Deleting nodes with 1 child
	- Link the child with the parent
	- Then delete self
- Deleting nodes with 2 children
	- Must replace itself. Who to replace with? **The minimum of the right (greater) child!**
	- Then delete self



### AVL Tree Balancing
Binary Search Tree complexity

| Operation                  | Time Complexity |
| -------------------------- | --------------- |
| Insert                     | O(h)            |
| Delete                     | O(h)            |
| Search                     | O(h)            |
| Find maximum/min           | O(h)            |
| Find predecessor/successor | O(h)            |
| In-order-traversal         | O(N)            |
h is the height of the tree. It could be seen as the number of layers. h count starts from 0.
It can be seen that we want to minimise h.

Without balancing, h can be very high because the tree can be a list

### Setup:
- Augment the node
	- This means storing the height for each node
		- ![[Pasted image 20250207160048.png|200]]
- Define what is 'balanced'
	- `abs(v.left.height - v.right.height) <= 1`

Note that balancing is not only done for the top node, but EVERY node. For instance here, the node that is out of balance is '29' and '20'
![[Pasted image 20250207160210.png|200]]


### Rotation

**Note how balance is not about the NUMBER of nodes, but the height**
![[Pasted image 20250207200442.png|300]]
Use this type of calculation

- Left-rotate -> The root node moves to the left
	- Requires a right child
	- Right child moves up, root node moves down
	- The left child node of the right child node of the root node is moved to the be the right of the new child node
![[Pasted image 20250207200727.png|200]]
- Right-rotate -> The root node moves to the right
	- Requires a left child
	- Same idea: right child node of the right child node of the root node is to be the left child node of the shifted root node 
![[Pasted image 20250207200936.png]]
For instance, 29 -> 32 -> 37 above
The use left-rotate because 32 is a right child of 29.
It then becomes 29 <- 32 -> 37



There are 6 possible cases:
- A is left-heavy
	- B is left-heavy -> Right-rotate A 
	- B is right-heavy -> Left-rotate B, Right rotate A
	- B is balanced -> Right-rotate A
- A is right-heavy
	- B is left-heavy -> Right-rotate B, Left-rotate A
	- B is right-heavy ->  Left-rotate A
	- B is balanced -> Left-rotate A
One can observe how they are reflections of each other
.
```
If v is left-heavy (MUST BE UNBALANCED):
	if v.left is right heavy (MAY NOT BE UNBALANCED): left-rotate(v.left)
	right-rotate(v)
```
```
If v is right-heavy (MUST BE UNBALANCED):
	if v.right is left-heavy (MAY NOT BE UNBALANCED): right-rotate(v.right)
	left-rotate(v)
```
**`left/right-heavy` DOES NOT equate to unbalanced!!!!!**
#### Insertion with balancing
- Insert key in BST
- Walk up the tree, balancing if need be


#### Deleting with balancing
- From the deleted node, walk up and check balance

![[Pasted image 20250226180856.png]]

### Hashing
Create a table using an array. Have a hash function. Store (A , B) key-value pair in the array. Location is decided using the hash function

### Hash Collision
- When the hash function results in the same number (ie storage)
	- However, keys WILL collide

**Solutions**
- Finding a good hash function
	- Difficult
	- Need to copy the entire database over
- Chaining
- Open addressing


##### Chaining
- Linked list of items to the same array unit
- Array becomes an array of linked list
- Potential issue:
	- Deleting requires search
	- Searching requires going through the entire linked list. Worst case, O(N)
BUT LETS ASSUME THAT EACH HASH VALUE HAS THE SAME PROBABILITY OF BEING HASHED TO BECAUSE WE WANT TO MAINTAIN SANITY.
![[Pasted image 20250207205014.png]]


#### Using Good Hash Functions
- Division method
- Multiplication method

$h(k)=k \mod m$ 
Use m values that are prime numbers
![[Pasted image 20250207205315.png]]
Issue: Division is slow


**Multiplication method**
- Fix table size m = 2^r
- Fix word size: w, size of a key in bits
- Fix (odd) constant A
$h(k)=(Ak) \mod 2^w >> (w-r)$



### Open Addressing
Find another bucket for the new item upon collision. Probe a sequence of buckets until you find an empty one. NO LINKED LIST.


There are multiple types of probing
- Linear probing (i+=x)
- Quadratic probing (i += 2^2, 3^2, etc)
- Double hashing
	- h(key,i) = h(key) + i × g(key)


**Do not set deleted items to NULL**
When using **open addressing** (linear probing, quadratic probing, etc.), the search procedure relies on finding an **empty slot (i.e., `null`)** to conclude that the key does not exist. If you remove an item by simply resetting its slot to `null`, then any keys that were originally “pushed further down” by collisions become unreachable—the search will stop prematurely at that `null` slot.



# Hash Table
- How large do we need our table to be?
- If size < 2n, too many collisions
- If size > 10n, too much wasted space
But we don't know n in advance.

So we change the size on the fly!
Grow as necessary, shrink if need be.

TLDR: 
- Double the size if (n == size)
- Half the size if (n < size / 4) (we still need filler space to distribute the probability of collision)

Idea: Subdivide the entire space by a binary tree
– Each internal node is a division of a partition/space
– Each leaf is a part of the space with only one polygon


A priority queue does not imply binary tree. A priority queue is simply that: a datastructure that maintains a set of prioritized objects by having functions: `insert` and `extractMin/Max`

A priority queue can be implemented with sorted or unsorted arrays too. However, it is clear that this is very inefficient. Sorted arrays take O(n) to insert. Unsorted arrays take O(n) to extract.

Instead, we use a binary heap that stores items in a tree.
This is an example of a minimum heap. The minimum element is at the top.
![[Pasted image 20250226161241.png| 200]]

This reduces the insertion to O(logN) and extraction to O(logN).
This is because a heap must be a completed binary tree, with the SOLE exception of the last level. This results in height of O(logN)
Additionally, the parent must have a higher priority (larger or smaller) than the child. 

![[Pasted image 20250209170011.png|300]]

It is important to note that the value of left and right child with respect to each other DOES NOT matter here unlike AVL. Left side does not have to be bigger than right or vice-versa. The main comparison is to the parent instead. Because of this, we don't need to do rotation (YAY)


**Storing a tree in an array:**
Let the height be h, starting from 0, and the element be the nth element of the row (starting from n=0)
$2^{h}-1+n$

left = 2x+1
right = 2x+2
parent = floor((x-1)/2)

**Inserting into heap**
Add a new leaf to the bottom and bubble up.

**Deleting the middle/root**
```
Suppose the Heap is a Max-Heap as:  
        22
       /  \
      5    18
     / \   /  \
    4   3 15   7
   / \   \
  1   2   2

The element to be deleted is 5

The last element is 2.  
 Replace the last element with 5, and delete it.  
        22
       /  \
      2    18
     / \   /  \
    4   3 15   7
   / \   
  1   2     5(Bye)

Heapify again.  
Final Heap:  
        22
       /  \
      4    18
     / \   /  \
    2   3 15   7
   / \   
  1   2 (equal is ok)

```

**Heapsort**
Unsorted list -> Heap: O(n)
Heap array -> Sorted list: O(n log n)
**O(n log n) time worst-case**
- Fast
	- Faster than mergesort
	- slightly slower than quicksort
- Deterministic - always NlogN
- Unstable

![[Pasted image 20250226162428.png]]


![[Pasted image 20250226160949.png|300]]

TLDR:
In implementation, if possible we should do weighted-union with path compression. However, in reality, that is sometimes hard(er) to implement. Path compression is very simple. Use path compression :)



# Storing data
 if graph is dense then use an adjacency matrix; else use an adjacency list.

Adjacency Matrix (space complexity is high)
– Fast query: are v and w neighbors?
– Slow query: find me any neighbor of v.
– Slow query: enumerate all neighbors.
Adjacency List:
– Fast query: find me any neighbor.
– Fast query: enumerate all neighbors.
– Slower query: are v and w neighbors?


Degree -> The number of adjacent nodes to the node
Diameter -> The maximum shortest distance between two nodes
![[Pasted image 20250225214003.png|300]]

Clique -> All nodes are connected to other nodes
Cycle -> Degree = 2 and diameter = (n/2) or (n/2 - 1)


How to find: Lower bound of diameter-> Generate an example that requires at least n moves -> This would mean that the actual diameter has to be >= n 


How to check: Upper bound of diameter -> Enumerate all possible combinations and show that none is more than n


Adjacency list -> List of list
Adjacency matrix -> 2D matrix

Benefits and cost? Which is faster at what?
Adjacency list -> Good space complexity, slow to show relation between n and m, **enumerating all neighbours**
Adjacency matrix -> Bad space complexity, show relation between n and m quickly, **fast query**

DFS code. 
```c++
#include <bits/stdc++.h>
using namespace std;
 
// Graph class represents a directed graph

class Graph {
public:
    map<int, bool> visited;
    map<int, list<int> > adj;
 
    void addEdge(int v, int w);
    void DFS(int v);
};
 
void Graph::addEdge(int v, int w)
{
// using adjacency list representation
    adj[v].push_back(w); // Add w to v’s list.
}
 
void Graph::DFS(int v)
{
    // Mark the current node as visited and
    // print it
    visited[v] = true;
    cout << v << " ";
 
    // Recur for all the vertices adjacent
    // to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFS(*i);
}
 
// Driver code
int main()
{
    // Create a graph given in the above diagram
    Graph g;
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
 
    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    g.DFS(2);
 
    return 0;
}
```


BFS code. Use Queue.
```c++
#include<iostream>
#include <list>
 
using namespace std;
 
class Graph
{
    int V;    // No. of nodes
    list<int> *adj;  
public:
    Graph(int V); 
    void addEdge(int v, int w);
    void BFS(int s); 
};
 
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
 
void Graph::addEdge(int v, int w)
{
//This class represents a directed graph using
    adj[v].push_back(w); // Add w to v’s list.
}
 
void Graph::BFS(int s)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;
 
    list<int> queue;
 
    // Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);
 
    // 'i' will be used to get all adjacent
    // vertices of a vertex
    list<int>::iterator i;
 
    while(!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        for (i = adj[s].begin(); i != adj[s].end(); ++i)
        {
            if (!visited[*i])
            {
                visited[*i] = true;
                queue.push_back(*i);
            }
        }
    }
}
 
// Driver program to test methods of graph class
int main()
{
    // Create a graph given in the above diagram
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
 
    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) \n";
    g.BFS(2);
 
    return 0;
}
```


**When does BFS not work?**
It does not work when the graphs are disconnected.  


**What is a directed graph**
Each edge is directed. This is unlike undirected graph where node 1 <-> node 2. Edges can be one way.

There will be slight modifications to the adjacency matrix/list. 

# DAG


SSSP algorithms find the shortest paths from a starting vertex to all other vertices in a graph

# SSSP (Single Sourced Shortest Path) 

Shortest path for weighted graphs
Weighted graphs may be cyclic or acyclic.

There are many possible types of queries:
- Find shortest distance from A to B
- Find shortest distance from A to all other nodes
- Find shortest distance for every possible combination of node pairs.

`relax(u,v)` is a function that changes the `dist[v]` to `dist[v] = dist[u] + weight(u,v)` if `dist[v]` is greater.

```c++
relax(int u, int v){
	if (dist[v] > dist[u] + weight(u,v)) dist[v] = dist[u] + weight(u,v);
}
```

**Dijkstra's**
Cannot handle negative weight

Can answer:
How far is it from S to D?
What is the shortest path from S to D
Find the shortest path from S to every node
```c++
```

**Bellman-Ford**
Can handle negative weight and can detect negative cycles too.
To detect negative cycles, count the number of traversals done. If it is the Vth relaxation, there is a negative cycle where V is the number of vertices (node). 
Why?
Let us consider the longest shortest path. It is a line of V nodes. It will require maximum V-1 relaxation. So if it is the Vth relaxation, negative cycle is detected.

**Run bellman ford for v+1 iterations. if there is a change between vth iteration and v+1 iteration, there is a negative cycle**

Why don't we consider positive cycles? Because it doesn't matter in Bellman-Ford as the positive cycle would needlessly add to the existing value, which would mean that the value does not change because the new value will always be larger.

```c++
struct Edge{

}
```


Suppose you have a bunch of actions (nodes). To visit A, you must visit B first. Topological sort is to find a good sequence.

**Topological Order:**
Sequential total ordering of all nodes
Edges only point forward

**Only works for directed acyclic graph (DAG)**
Acyclic means that there is no cycle. Graph has to be directed.


To do DAG topological sort, we do DFS with Post-order 


```c++
#include <iostream>
#include <list>
#include <stack>
using namespace std;
  
// Class to represent a graph
class Graph {
    int V; // No. of vertices'
  
    // Pointer to an array containing adjacency listsList
    list<int>* adj;
  
    // A function used by topologicalSort
    void topologicalSortUtil(int v, bool visited[], stack<int>& Stack);
  
public:
    Graph(int V); // Constructor
  
    // function to add an edge to graph
    void addEdge(int v, int w);
  
    // prints a Topological Sort of the complete graph
    void topologicalSort();
};
  
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
  
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}
  
// A recursive function used by topologicalSort
void Graph::topologicalSortUtil(int v, bool visited[],
                                stack<int>& Stack)
{
    // Mark the current node as visited.
    visited[v] = true;
  
    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            topologicalSortUtil(*i, visited, Stack);
  
    // Push current vertex to stack which stores result
    Stack.push(v);
}
  
// The function to do Topological Sort. It uses recursive
// topologicalSortUtil()
void Graph::topologicalSort()
{
    stack<int> Stack;
  
    // Mark all the vertices as not visited
    bool* visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
  
    // Call the recursive helper function to store Topological
    // Sort starting from all vertices one by one
    for (int i = 0; i < V; i++)
        if (visited[i] == false)
            topologicalSortUtil(i, visited, Stack);
  
    // Print contents of stack
    while (Stack.empty() == false) {
        cout << Stack.top() << " ";
        Stack.pop();
    }
}
  
// Driver program to test above functions
int main()
{
    // Create a graph given in the above diagram
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
  
    cout << "Following is a Topological Sort of the given graph n";
    g.topologicalSort();
  
    return 0;
}
```


Prim's algorithm
Kruskal's algorithm
Boruvka's algorithm


![[Pasted image 20250422124447.png]]


The convex hull of a simple polygon **encloses the given polygon and is partitioned by it into regions, one of which is the polygon itself**. The other regions, bounded by a polygonal chain of the polygon and a single convex hull edge, are called pockets.

![[Pasted image 20250225181435.png]]

**Jarvis' March**

Chooes the leftmost node. Imagine a pointer pointing south. Find the node with the least turning angle. This can be imagined using a line and sweeping anticlockwise until a node is hit. Move to that node. Repeat

![[Pasted image 20250225181936.png|300]]

Time complexity: O(h x n). where h is the number of hull points (thus h) and n is the number of input nodes. Worst case complexity is O(n * n) when h=n. 
Complexity is because each time we move to a new hull point, we need to scan all existing nodes. This includes nodes that are already included because in the final step we need to 'close' up the polygon by connecting the hull point h-1 to an existing hull point.

**Graham Scan**

Choose the leftmost node. Sort the rest based on the angle relative to that node. Starting from that node, walk anticlockwise. You are now on node w (standing for walking).
Observe all the angles of other nodes from node w. Is any of them convex corner, fill it and walk back.
A better description of the last step: 
	At each step, before adding in the next hull point, the algorithm checks whether the last two points added to the convex hull forms a convex corner with the hull point. If they do, pop the last one. Then add in the hull point. 


![[Pasted image 20250225182810.png|300]]
Time complexity: O(nlogn)
Step 1, finding the leftmost node is O(n)
Step 2, sorting is O(nlogn)
Step 3, removing the convex corners is O(n). Using a list, we can see that reversing is O(n) because you only have to do it once. Each check is only 3-4 operations 
	- Get the last two points in the list
	- Calculate if it is a convex corner
	- If yes, pop
	- Then append hull point.


**Divide and Conquer (Quick Hull)**
Sort based on a direction (like y-direction) => O(nlogn)

Find median and partition
Recurse on left and right
Somehow merge them together


Merging is done using the property of two convex polygons: they will have four tangents. We are concerned with two - the top and bottom
![[Pasted image 20250225184931.png]]
After getting the shape, merge using this idea. Delete the middle section. You have a bigger convex hull now. Repeat.

O(nlogn). 
**Incremental Method**
Sort based on a selected direction.
Add a point sequentially. After adding, check if any points are 'inside'. Remove those points.
![[Pasted image 20250225184422.png|300]]



**Quickhull**

Construct a quadrilateral with the four extreme points (extreme x,y)
Discard all points inside.
For each side, find the furthest point (extreme x and y)
Include in convex hull
Remove anything inside
Repeat

Worst case: O(n^2) 
Circle!
![[Pasted image 20250225185552.png]]



Linked list of linked list for notepad apps