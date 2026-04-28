========================================================================================================================
Distributed Quantum Error Correction via Circuit Cutting: Running a 3-Qubit Repetition Code on Real IBM Quantum Hardware
========================================================================================================================
 
*By Christopher Poon*
 
----
 
Introduction
============
 
Quantum computers are currently in the Noisy Intermediate-Scale Quantum (NISQ) era. Unlike classical transistors which flip between 0 and 1 with an error rate around :math:`10^{-27}`, quantum bits (qubits) fail with a probability closer to :math:`10^{-3}-10^{-4}`. This is a fundamental consequence of what makes quantum computing powerful. Qubits exist in superposition, entangle with each other, and interact with their environment. These very properties that make quantum computers useful also make them fragile to external noise, temperature, vibration, etc.
 
As a result, every quantum computation you run accumulates errors. If you run a shallow quantum circuit, less noise is introduced. Run the same kind of deep circuit needed for quantum advantage, such as for Shor's algorithm, the errors will dominate the result. 

The solution is **Quantum Error Correction (QEC)**. Generally, we encode one logical qubit into multiple physical qubits, add redundancy, and use that redundancy to detect and fix errors without ever measuring the data directly. However, the most basic codes, like the 3-qubit repetition code, require 3 physical qubits per logical qubit, reducing the number of qubits you can leverage by 3 per qubit. More sophisticated codes like the surface code require hundreds of physical qubits per logical qubit. IBM's largest chip, IBM Condor, has 1,121 qubits.
 
This is where **Distributed Quantum Computing (DQC)** enters the picture. Instead of scaling monolithic (single) chips, what if you connected many smaller quantum processors together? Each QPU handles a portion of the computation, and the results are combined. However, connecting quantum processors is an ongoing research problem.
 
In this project, I explore the usage of circuit cutting, implemented using IBM's `qiskit-addon-cutting` library, to simulate what distributed quantum error correction would look like and then run it on real IBM Quantum hardware through RPI's IBM Quantum System One.
 
----

Problem Description
===================
 
The 3-qubit repetition code encodes one logical qubit as:

:math:`\ket{\psi} = \alpha\ket{0} + \beta\ket{1}  \rightarrow  \alpha\ket{000} + \beta\ket{111}`
 
Two CNOT gates entangle the state from qubit A to qubits B and C. We encode the quantum state this way because the no-cloning theorem forbids copying a quantum state. After encoding, any single bit-flip error changes the state in a detectable way:

:math:`\text{Qubit A flipped: }  \alpha\ket{100} + \beta\ket{011} \rightarrow  \text{ syndrome $11$}`

:math:`\text{Qubit B flipped: }  \alpha\ket{010} + \beta\ket{101} \rightarrow  \text{ syndrome $10$}`

:math:`\text{Qubit C flipped: }  \alpha\ket{001} + \beta\ket{110} \rightarrow  \text{ syndrome $01$}`

:math:`\text{No error: }  \alpha\ket{000} + \beta\ket{111} \rightarrow  \text{ syndrome $00$}`
 
Phase-flip errors are handled by encoding in the X basis instead: :math:`\alpha\ket{+++} + \beta\ket{---}`, where a Z error plays the same role that an X error plays in the computational basis.
 
**The problem** is that the encoding CNOTs that create :math:`\alpha\ket{000} + \beta\ket{111}` are the gates that need to cross QPU boundaries. Qubit A is on QPU Alice, qubit B is on QPU Bob, qubit C is on QPU Charlie. How do you apply CNOT from qubit A to qubit B when A and B are on separate physical machines?
 
Babaie and Qiao [1]_ use quantum teleportation via Bell pairs. My approach uses circuit cutting and partitioning.

----

References
==========

.. [1] Babaie, S. & Qiao, C. (2024). *Towards Distributed Quantum Error Correction for Distributed
   Quantum Computing.* arXiv:2409.05244.
 
.. [2] Tang, W., Tomesh, T., Suchara, M., Larson, J., & Martonosi, M. (2021). *CutQC: Using Small
   Quantum Computers for Large Quantum Circuit Evaluations.* ASPLOS 2021.
 
.. [3] IBM Quantum. *Qiskit Addon: Circuit Cutting Documentation.*
   https://qiskit.github.io/qiskit-addon-cutting
 
.. [4] Sutcliffe, E., Jonnadula, B., Le Gall, C., Moylett, A. E., & Westoby, C. M. (2025).
   *Distributed quantum error correction based on hyperbolic floquet codes.* IEEE QCE 2025.
 
.. [5] Wong, T. G. (2023). *Introduction to Classical and Quantum Computing.*
   https://www.thomaswong.net/introduction-to-classical-and-quantum-computing-1e4p.pdf

----
 
.. note::
 
   Portions of this article were drafted with assistance from Claude (Anthropic). The author takes
   full responsibility for all technical content, experimental results, analysis, and conclusions
   presented.
