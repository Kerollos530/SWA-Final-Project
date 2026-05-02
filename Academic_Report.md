# Academic Report: Online Pet Store Management System

## 1. Project Overview
**Course:** Software Architecture (SWA)  
**Project Title:** Online Pet Store Management System  
**Implementation Language:** Python  
**Architecture Style:** Object-Oriented Architecture with Design Patterns  

---

## 2. Introduction
In modern software engineering, the architecture of a system defines its scalability, maintainability, and efficiency. This project demonstrates a robust architectural approach to a Pet Store Management System by implementing three core Design Patterns: **Singleton**, **Factory**, and **Observer**. These patterns are strategically chosen to solve common structural and behavioral challenges in software development.

---

## 3. System Features
The system provides a simplified yet functional interface for:
*   **Inventory Management:** Centralized storage of various product categories.
*   **Dynamic Product Creation:** Handling different types of items like Pets, Food, and Accessories.
*   **Order Tracking:** Real-time monitoring of order fulfillment status.
*   **Notification System:** Automated updates pushed to customers regarding their purchases.

---

## 4. Design Patterns Implementation

### A. Singleton Pattern (Creational)
*   **Component:** `DatabaseManager` class.
*   **Definition:** Ensures that a class has only one instance and provides a global point of access to it.
*   **Justification:** In a management system, having multiple instances of a database handler can lead to data inconsistency and memory overhead. The Singleton pattern ensures all parts of the application interact with a single, synchronized data source.

### B. Factory Pattern (Creational)
*   **Component:** `ProductFactory` class.
*   **Definition:** Provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
*   **Justification:** The store deals with various product types (Pet, Food, Accessory). By using a Factory, we decouple the client code from the specific classes. Adding a new product type (e.g., "Medicine") only requires a change in the factory, making the system highly extensible.

### C. Observer Pattern (Behavioral)
*   **Component:** `Order` (Subject) and `Customer` (Observer).
*   **Definition:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
*   **Justification:** Instead of the customer repeatedly checking the order status (polling), the Observer pattern allows the system to "push" updates. This reduces computational waste and improves the user experience.

---

## 5. Architectural Benefits
The integration of these patterns results in a **Loose Coupling** between components and **High Cohesion** within each class. 
*   **Maintainability:** Each pattern addresses a specific concern, making the code easier to debug.
*   **Scalability:** The system can grow in complexity (more products, more notification types) without breaking the existing core logic.
*   **Readability:** Following industry-standard patterns makes the code self-documenting for other architects.

---

## 6. Conclusion
The Online Pet Store Management System serves as a practical application of Software Architecture principles. By moving beyond simple procedural code and adopting recognized Design Patterns, we have created a solution that is professional, scalable, and aligned with modern software engineering standards.

---
**Prepared by:** [Your Name / Team Name]  
**Date:** May 2026
