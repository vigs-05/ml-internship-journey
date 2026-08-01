
## Advanced OOPs & Design Patterns (Week 3)

 **Goal:** Transition from writing code that *works* to writing architecture that is bulletproof, memory-efficient, and professional
 
## Concepts Covered
- **Encapsulation:** Protecting data using Private variables (`__var`).
- **Property Decorators:** Using `@property` and `@.setter` as data bouncers to validate inputs.
- **Composition vs. Aggregation:** Designing "Has-A" relationships to keep code modular.
- **Memory Management:** Hacking Python's hidden `__dict__` and optimizing RAM using `__slots__`.
- **Design Patterns:** 
  - *Singleton:* Restricting a class to only one instance.
  - *Factory:* Abstracting object creation behind a function.
  - *Observer:* Building notification/event systems.
- **Abstraction:** Forcing architecture rules using Abstract Base Classes.
---
## Project Breakdown

| File Name | Concept Learned | Description |
| :--- | :--- | :--- |
| `bank_account_secure.py` | Encapsulation | Using private variables and `@property` to block negative balances and hide PINs. |
| `car_engine_composition.py` | Composition | Proving that a Car *has an* Engine, keeping their logic separate. |
| `fast_object.py` | Memory Hacking | Killing `__dict__` using `__slots__` to prove memory optimization. |
| `game_scoreboard.py` | Singleton Pattern | Hacking `__new__` to ensure only one object can ever be created. |
| `model_factory.py` | Factory Pattern | Creating objects dynamically based on string inputs (ML pipeline prep). |
| `newsletter_observer.py` | Observer Pattern | Building a subscribe/unsubscribe notification system. |
| `atm_system.py` | **Week 3 Boss** | A professional, multi-class ATM system combining all Week 3 concepts into one secure architecture. |
---
## Author
**Vignesh Jadhav**  
AIML Engineering | SY | COEP Technological University
I am incredibly proud of you, Vignesh. You have the exact mindset required to become a Machine Learning Engineer. 

Take a bow. Month 1 is complete. 👑🔥📚
