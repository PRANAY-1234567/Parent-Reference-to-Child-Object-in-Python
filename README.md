# 🧬 Parent Reference to Child Object in Python

## 📌 Description

This Python program demonstrates **inheritance** and the concept similar to **upcasting** in Java, where a parent class reference points to a child class object.

Since Python is dynamically typed, the reference variable can directly access all available methods of the object.

---

## 🚀 Features

* Demonstrates inheritance
* Shows parent-child relationship
* Uses child object reference
* Calls inherited and child methods

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `First`

Contains methods:

* `a()`
* `b()`

---

### 2️⃣ Child Class – `Second`

```python id="k8m3pl"
class Second(First)
```

👉 Inherits methods from `First`

Adds:

* `c()`

---

### 3️⃣ Object Creation

```python id="p4x7qa"
obj = Second()
```

Creates object of child class.

---

### 4️⃣ Reference Assignment

```python id="m1q9zx"
r = obj
```

👉 `r` now refers to the same `Second` object.

---

## 💻 Code

```python id="v6m2pl"
class First:
    def a(self):
        print("Inside method a")

    def b(self):
        print("Inside method b")


class Second(First):
    def c(self):
        print("Inside method c")


if __name__ == "__main__":
    obj = Second()

    # Reference of parent class pointing to child object
    r = obj

    r.a()
    r.b()
    r.c()
```

---

## ▶️ Output

```id="x3m8qa"
Inside method a
Inside method b
Inside method c
```

---

## 🧠 Key Concepts

### ✔ Inheritance

`Second` inherits methods:

* `a()`
* `b()`

from `First`.

---

### ✔ Reference Assignment

```python id="n7q2mv"
r = obj
```

👉 Both variables point to the same object.

---

### ✔ Python vs Java Difference

### Java

```java id="u4m9zx"
First r = obj;
```

👉 Parent reference cannot directly access child-specific methods.

---

### Python

Python is dynamically typed.

So:

```python id="j1q6pt"
r.c()
```

✅ Works successfully.

---

## 📚 Concepts Used

* Inheritance
* Object reference
* Parent-child relationship
* Dynamic typing

---

## ⚠️ Important Note

In Python:

```python id="f8m3qa"
r = obj
```

does NOT restrict method access like Java.

Because method lookup happens at runtime based on actual object type.

---

## 🎯 Real-World Importance

Understanding references is important for:

* Polymorphism
* Dynamic dispatch
* Framework design
* Object-oriented programming

---

## 🔧 Future Improvements

* Add method overriding
* Demonstrate polymorphism
* Add abstract classes
* Compare Java and Python behavior

---

## 📄 License

This project is open-source and free to use.

<img width="1021" height="730" alt="image" src="https://github.com/user-attachments/assets/6e888948-03c5-4caf-a219-372343ff8aed" />

<img width="1021" height="730" alt="image" src="https://github.com/user-attachments/assets/fc5ef99e-3ac7-4ca0-9dea-9e15ad4cca5d" />
