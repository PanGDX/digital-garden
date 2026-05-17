```latex
\documentclass[10pt,landscape]{article}

% --- PACKAGES ---
\usepackage[margin=0.25in]{geometry}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{graphicx}
% --- FONT & LAYOUT SETTINGS ---
\renewcommand{\familydefault}{\sfdefault} % Sans-serif font for readability at small sizes
\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}
\raggedright % Prevents bad spacing in narrow columns

% Section formatting for compactness
\titleformat{\section}{\scriptsize\bfseries\uppercase}{}{0pt}{}[\vspace{-2pt}\rule{\linewidth}{0.3pt}\vspace{-2pt}]
\titleformat{\subsection}{\scriptsize\bfseries}{}{0pt}{}
\titlespacing{\section}{0pt}{3pt}{2pt}
\titlespacing{\subsection}{0pt}{2pt}{1pt}

% Custom ultra-compact itemize
\newlist{compactitem}{itemize}{3}
\setlist[compactitem]{label=\textbullet, leftmargin=6pt, itemsep=0pt, parsep=0pt, topsep=0pt, partopsep=0pt}
\setlist[itemize]{leftmargin=6pt, itemsep=0pt, parsep=0pt, topsep=0pt, partopsep=0pt}

\begin{document}
\scriptsize % Sets font to ~7pt

\begin{multicols*}{5} % 5-column layout

\section{Object-Oriented (Java)}
\begin{compactitem}
    \item \textbf{Inheritance (IS-A):} Subclass instance can be assigned to superclass ref (\texttt{Animal a = new Dog();}). Compiler uses ref as a ``mask,'' restricting access to superclass methods only.
    \item \textbf{Type Safety:} Cannot assign superclass to subclass ref (\texttt{Dog d = new Animal();}). Object lacks subclass methods (e.g., \texttt{bark()}); causes crash.
    \item \textbf{Exceptions:} Only objects inheriting from \texttt{java.lang.Throwable} can be thrown. Strings are not Throwable.
\end{compactitem}

\section{UML Notation}
\begin{compactitem}
    \item \textbf{Abstract Classes:} Italicized or stereotyped. Standard text implies non-abstract.
    \item \textbf{Visibility:} Public (\texttt{+}), Private (\texttt{-}).
    \item \textbf{Multiplicity:} Defines instance connections (e.g., \texttt{1...*}, \texttt{0,1}).
    \item \textbf{Association Class:} Connects to an association relationship to add attributes/operations (e.g., \texttt{Payment} class for a User-Shop ``Pays'' relationship).
    \item Underlined (:Container): Represents an object (an instance of a class). 
    \item Not underlined (:Container or Container): static class
\end{compactitem}

\section{Methodology \& Arch}
\begin{compactitem}
    \item \textbf{Breadth-First (Iterative):} Evolves all major components in parallel (thin-slice).
    \item \textbf{Depth-First (Incremental):} Fully implements specific features one by one.
    \item \textbf{Waterfall:} Rigid, sequential (Req $\rightarrow$ Design $\rightarrow$ Code $\rightarrow$ Test). Best for stable reqs. In a pure Waterfall model, you do not release working software in phases but in one shot after gathering all requirements. 
    \item \textbf{n-Tier/Layered:} Divides app into horizontal layers (Pres, Biz, Data) to isolate responsibilities.
    \item \textbf{MVC:} Separation of Concerns via Data (Model), UI (View), Input (Controller).
    \item \textbf{CI/CD:} CI automates merge/test; CD automates release. (They are not the same).
    \item \textbf{User Story:} ``As a \textit{[Role]}, I want \textit{[Func]} so that \textit{[Benefit]}.''
    \item \textbf{Non-Functional Req:} e.g., ``Low Latency for Order Synchronization.''
    \item Breadth-First Development (BFD): or a "horizontal" approach, focuses on implementing all major components and architectural layers of a system in parallel 
\end{compactitem}

\section{Design Patterns}
\begin{compactitem}
    \item \textbf{Singleton:} Class has only 1 instance. Acts globally, increases coupling, hard to replace with stubs in testing.
    \item \textbf{Facade:} Simplified interface to complex internal classes. Hides internals (e.g., UI accesses Logic component via Facade without knowing it contains a Book class).
\end{compactitem}

\section{Design Principles}
\begin{compactitem}
    \item \textbf{SRP:} Single Responsibility. 1 reason to change.
    \item \textbf{OCP:} Open for extension, Closed for modification. Fixes poor extensibility.
    \item \textbf{LSP:} Liskov Sub. Derived classes must substitute base classes. Violations: Subclass throwing new error, or reducing capability.
    \item \textbf{ISP:} Interface Segregation. Don't force clients to depend on unused methods.
    \item \textbf{DIP:} Dependency Inversion. High \& low modules depend on abstractions, not details.
    \item \textbf{Law of Demeter (LoD):} Least knowledge. Object only calls methods of itself, params, created objs, or direct fields (immediate friends).
    \item \textbf{DRY:} Don't Repeat Yourself. Single authoritative representation.
    \item \textbf{YAGNI:} You Aren't Gonna Need It. Don't code for hypothetical futures.
\end{compactitem}

\section{Testing \& QA}
\begin{compactitem}
    \item \textbf{System vs Acceptance:} System checks tech specs/edge cases (heavy pos/neg testing). Acceptance (by client) validates biz reqs (happy-paths).
    \item \textbf{Dynamic Analysis:} Requires executing code (e.g., code coverage tools).
    \item \textbf{Static Analysis:} Inspects code without running it.
    \item \textbf{Equivalence Partitioning:} Group inputs behaving similarly. Test boundaries (0, 1, MAX). One issue per partition. NULL is an option.
    \item \textbf{Defensive Prog:} Runtime checks (null-checks) to prevent crashes (adds slight execution time).
    \item \textbf{Positive Test:} Valid inputs $\rightarrow$ Success.
    \item \textbf{Negative Test:} Invalid inputs $\rightarrow$ Throws exception (e.g., quantity=0).
    \item \textbf{Stub:} Simple hardcoded implementation mimicking responses for testing. Replaces complex components.
    \item \textbf{Tools:} \textbf{JUnit} = Testing framework. \textbf{Gradle} = Build tool (compile/test/pack). \textbf{Jenkins/GH Actions} = CI platforms that trigger tools.
\end{compactitem}

\section{Clean Code \& Standards}
\begin{compactitem}
    \item \textbf{lowerCamelCase:} Locals, Params, Fields.
    \item \textbf{UPPER\_SNAKE\_CASE:} Constants.
    \item \textbf{Booleans:} Prefix with \texttt{is}, \texttt{has}, \texttt{can}.
    \item \textbf{Issues:} Magic Strings/Nums (use constants), Indentation, Input validation, Missing SRP.
    \item \textbf{Comments:} Explain ``Why,'' not ``What''. Javadocs should start with \textit{``Returns the text...''}
\end{compactitem}

\section{Glossary \& Misc}
\begin{compactitem}
    \item \textbf{Abstraction:} Suppress complex details below level of interest.
    \item \textbf{Actor:} User role (human/system) outside system.
    \item \textbf{Architecture:} High-level structures/relations.
    \item \textbf{Brainstorming:} Generate diverse/creative ideas.
    \item \textbf{Brooks' Law:} Adding people to late project makes it later.
    \item \textbf{CLI App:} Command Line Interface application.
    \item \textbf{Coupling:} Degree of interdependence between modules.
    \item \textbf{Domain Expert:} Discipline expert (e.g., Accountant for accounting app).
    \item \textbf{Dynamic Binding:} Late binding; methods resolved at runtime.
    \item \textbf{Static Binding:} Early binding; resolved at compile time.
    \item \textbf{Enterprise App:} High demands (scale, perf, sec).
    \item \textbf{Exception:} Event disrupting normal flow.
    \item \textbf{Feature List:} Grouped by aspect, priority, delivery.
    \item \textbf{Focus Group:} Informal interview in interactive group.
    \item \textbf{Glossary:} Ensures common stakeholder understanding of terms.
    \item \textbf{Pair Programming:} Driver writes code, Observer/Navigator reviews. Switch frequently.
    \item \textbf{Polymorphism:} Diff objects respond own way to identical messages.
    \item \textbf{Prototype:} Mockup to get feedback, validate tech (proof-of-concept), or field-test.
    \item \textbf{Type Signature:} Parameter type sequence (order matters). Return type/param names are \textbf{not} part of it.
    \item \textbf{Use Case:} Sequence of actions yielding observable result. Contains Main flow \& Extensions (e.g., 3a. Camera blocked $\rightarrow$ notify $\rightarrow$ user unblocks $\rightarrow$ resume).
\end{compactitem}

\subsection{Git / VCS}
\begin{compactitem}
    \item \textbf{Commit:} (v) saving change to history, (n) a revision.
    \item \textbf{Stage:} Instruct Git to prep file for commit.
    \item \textbf{RCS:} Revision Control Software automates tracking.
    \item \textbf{Repo:} DB of history tracked by RCS.
    \item \textbf{Working Dir:} Root directory revision-controlled by Git.
\end{compactitem}

\section{1. QA \& Testing}
\textbf{QA = Validation + Verification}
\begin{itemize}
    \item \textbf{Validation:} Building the \textit{right system}? (Reqs correct?)
    \item \textbf{Verification:} Building the \textit{system right}? (Implemented correctly?)
\end{itemize}

\subsection{Testing Levels}
\begin{itemize}
    \item \textbf{Unit Testing:} Test individual units (methods/classes).
    \item \textbf{Integration Testing:} Test if parts \textit{work together}. Focuses on interactions (e.g., use stubs for Engine/Wheel, then test real pieces integrated).
    \item \textbf{System Testing:} Test whole system against the \textit{system specification}. Focuses on external behavior. Done by QA team. Tests Non-Functional Reqs (NFRs) like load/security, and graceful failure beyond limits.
    \item \textbf{Acceptance (UAT):} Ensure it meets \textit{user reqs}. Done by user/customer team on deployment site.
\end{itemize}

\subsection{Testing Types \& Approaches}
\begin{itemize}
    \item \textbf{Alpha:} Users test in controlled developer env.
    \item \textbf{Beta:} Subset of target users test in natural setting.
    \item \textbf{Dogfooding:} Creators use own product.
    \item \textbf{Scripted:} Pre-written systematic test cases. High coverage but slow.
    \item \textbf{Exploratory:} Ad-hoc, on-the-fly. Fast but might miss edge cases. (Doing both is ideal).
    \item \textbf{Regression:} Re-testing to detect unintended effects after mods. Best automated.
        \begin{itemize}
            \item \textbf{TestFX:} Automates JavaFX UI.
            \item \textbf{Visual Studio:} Record-replay GUI automation.
            \item \textbf{Selenium:} Automates web app UIs.
        \end{itemize}
    \item \textbf{Test-Driven Dev (TDD):} Write tests \textit{before} SUT (System Under Test). Cycle: Red (fail) $\rightarrow$ Green (pass) $\rightarrow$ Refactor. Evolves in increments.
\end{itemize}

\subsection{Coverage \& Strategies}
\textbf{Test Coverage:} Metric for code exercised by tests.
\begin{itemize}
    \item \textbf{Function/Method:} \% of functions executed.
    \item \textbf{Statement:} \% of LOC executed.
    \item \textbf{Decision/Branch:} If-statements evaluate to both true/false (tests actual control flow branches).
    \item \textbf{Condition:} Every boolean sub-expression evaluated true/false. (Not same as decision).
\end{itemize}
\textbf{Combinatorial Strategies:}
\begin{itemize}
    \item \textbf{All combinations:} Every unique combo of inputs.
    \item \textbf{At least once:} Each test input used $\ge 1$ times. Heuristic: Valid inputs $\ge 1$ time in a positive test; test invalid inputs individually before combining.
    \item \textbf{All pairs:} All combos for any given \textit{pair} of inputs are tested. Optimizes coverage vs execution time.
\end{itemize}
\textbf{Test Data Selection:} Equivalence partitions (grouping inputs with same behavior) \& Boundary values (testing edges).

\textbf{Formal Verification:} Uses mathematical techniques to prove correctness. Highly specialized/expensive. Used in safety-critical software (flight control).

\section{2. Code Quality \& Maint}

\subsection{Code Review \& Analysis}
\textbf{Code Review:} Systematic exam to improve code.
\begin{itemize}
    \item PRs, Pair Programming, Formal Inspections.
\end{itemize}
\textbf{Analysis Tools:}
\begin{itemize}
    \item \textbf{Static Analysis:} Examines unexecuted code (unused vars, style errors). IDEs do this live. Java tools: CheckStyle, PMD, FindBugs.
    \item \textbf{Linters:} Subset of static analyzers for "cleaner" code.
    \item \textbf{Dynamic Analysis:} Requires execution. Gathers performance/memory stats.
\end{itemize}
\textbf{Debugger Tool:} Pauses execution, step-through line-by-line, inspect internal state. \textit{Recommended bug-fixing approach.}

\subsection{Refactoring}
Restructuring code in small steps without modifying external behavior. First write working code, then improve quality.
\begin{itemize}
    \item \textbf{NOT Rewrite/Bug-fix:} Does not alter external behavior or discard entire codebases.
    \item \textbf{Benefits:} Hidden bugs become visible, simpler code runs faster/easier for compiler to optimize.
    \item \textbf{Examples from Catalogs:} Consolidate Duplicate Conditional Fragments (move shared code outside `if`), Remove double negative, Replace magic literal, Replace param with explicit methods.
\end{itemize}

\subsection{Documentation}
\begin{itemize}
    \item \textbf{Dev-as-user:} How to reuse your component.
    \item \textbf{Dev-as-maintainer:} Explaining complex internals.
    \item \textbf{Four types:} Tutorials, How-to guides, Explanations, References.
    \item \textbf{JavaDoc:} HTML API generation. Classes: "Represents...". Methods: "Returns..." or "Performs...". Explain all params, returns, and throws.
\end{itemize}

\section{3. Reuse \& Infrastructure}
\textbf{Reuse risks:} Overkill (sledgehammer for a nut/bloat), lack of maturity (risk of dying off), restrictive licenses, bugs/vulnerabilities, malicious compromised dependencies.

\subsection{Mechanisms}
\begin{itemize}
    \item \textbf{Library:} Modular, general code used "as is".
    \item \textbf{API:} The contract/interface. For a class, it's the collection of public methods to invoke.
    \item \textbf{Framework:} Compartmentalized similarity. Implements default behavior. Facilitates adaptation/customization. Meant to be extended (e.g., Eclipse plugins, JUnit, JavaFX, Tkinter). Uses Inversion of Control.
    \item \textbf{Platform:} Provides a \textit{runtime environment}. Can bundle tools/libs. (e.g., JavaEE, .NET, OS).
\end{itemize}

\section{4. Requirements}
\begin{itemize}
    \item \textbf{Brownfield:} Replace/update existing system.
    \item \textbf{Greenfield:} Totally new system from scratch.
    \item \textbf{Stakeholder:} Anyone involved/affected (users, sponsors, devs, gov, interest groups).
\end{itemize}

\subsection{Types of Reqs \& Specs}
\begin{itemize}
    \item \textbf{Functional (FR):} What system should do.
    \item \textbf{Non-Functional (NFR):} Constraints on dev/ops. Includes: Business rules, constraints (budget/schedule), Tech (32/64-bit), Perf (resp time), Quality (novice usability), Process, Project Scope, Noteworthy points.
\end{itemize}

\textbf{Reqs Spec vs System Spec:}
\begin{itemize}
    \item \textbf{Reqs:} Normal conditions; terms of problems to solve; interface for intended end-users.
    \item \textbf{System:} Includes graceful failures; terms of how system solves problems; internal APIs for devs/testers.
\end{itemize}

\subsection{Elicitation \& Use Cases}
\textbf{Gathering methods:} Brainstorming, Surveys, Observation, Interview, Focus groups, Prototyping (validates tech \& gets feedback), Product surveys (study shortcomings).

\textbf{Use Cases (UC):} Interaction between Actor and System for specific functionality. Captures FRs.
\begin{itemize}
    \item \textbf{Step:} Gives actor's intention.
    \item \textbf{MSS (Main Success Scenario):} Standard flow.
    \item \textbf{Extensions:} Add-ons to MSS for alternative/exceptional flows (e.g., 3a happens after step 3; *a happens anywhere).
    \item \textbf{Include:} UC can include another UC (underlined).
    \item \textbf{Preconditions:} Required state before UC starts.
    \item \textbf{Guarantees:} Promised state after UC ends.
    \item \textbf{For Testing:} MSS is one test case, variations are others. UC lacks exact data, so tester applies equivalence partitions.
\end{itemize}
\textbf{Feature List:} Features grouped by aspect/priority.

\section{5. Design \& Architecture}
\begin{itemize}
    \item \textbf{Product/External Design:} User behavior. By UX/BAs.
    \item \textbf{Implementation/Internal Design:} Implementation tech. By Architects/Devs.
    \item \textbf{Approaches:} Top-down (high-level first, stable architecture), Bottom-up (components first, good for variations/repurposing), Mixed.
\end{itemize}

\subsection{Core Principles}
\textbf{Abstraction:} Suppressing lower-level complex details.
\begin{itemize}
    \item \textbf{Data Abstraction:} Thinking in bigger entities.
    \item \textbf{Control Abstraction:} Focusing on higher-level flow.
\end{itemize}
\textbf{Coupling \& Cohesion:}
\begin{itemize}
    \item \textbf{Coupling:} Measure of dependence. \textit{Low is good.} Strong coupling: change in X \textit{potentially} requires change in Y.
    \item \textbf{Cohesion:} Measure of related/focused responsibilities. \textit{High is good.} Keeps related tasks together, unrelated out.
\end{itemize}

\subsection{Patterns \& Architectures}
\textbf{Design Pattern Format:}
\begin{itemize}
    \item \textbf{Context:} Scenario/situation.
    \item \textbf{Problem:} Main difficulty to resolve.
    \item \textbf{Solution:} Core general details (requires refinement).
    \item \textbf{Anti-patterns:} Common wrong/inferior solutions.
    \item \textbf{Consequences:} Pros/Cons.
\end{itemize}
\textbf{Architectural Styles:} (Structure of specific system category, high scale reuse).
\begin{itemize}
    \item \textbf{Client-Server:} 1+ server, 1+ clients (Distributed).
    \item \textbf{Transaction Processing:} Workload divided into transactions handled by a \textit{dispatcher} (queuing, undo).
    \item \textbf{Service-Oriented (SOA):} Accessible services combined via centralized Enterprise Service Bus (ESB). E.g., XML web services. (NOTE: NOT microservices).
    \item \textbf{Event-Driven:} Detects events from \textit{emitters}, sends to \textit{consumers}. Flow controlled by events. Common in GUI.
\end{itemize}

\section{6. Process \& Management}
\subsection{SDLC Models}
\begin{itemize}
    \item \textbf{Sequential (Waterfall):} Linear progression through stages. Hard to pivot.
    \item \textbf{Iterative:} Goes through SDLC in iterations. Each iteration builds new version based on feedback.
\end{itemize}
\textbf{Agile Manifesto Principles:}
\begin{itemize}
    \item Individuals/interactions $>$ processes/tools.
    \item Working software $>$ comprehensive docs.
    \item Customer collab $>$ contract negotiation.
    \item Responding to change $>$ following a plan.
\end{itemize}
\textbf{Extreme Programming (XP):} Customer focus, teamwork, simplicity, feedback. Small repeated releases.

\textbf{Scrum Framework:}
\begin{itemize}
    \item \textbf{Scrum Master:} Maintains processes (pseudo-PM).
    \item \textbf{Product Owner:} Reps stakeholders/business.
    \item \textbf{Team:} Cross-functional execution (dev, test, design).
    \item \textbf{Sprints:} Iterations (1 week to 1 month). Yields potentially deliverable product increment.
    \item \textbf{Daily Scrum:} Key syncing practice.
\end{itemize}

\subsection{Project Management Tracking}
\begin{itemize}
    \item \textbf{WBS (Work Breakdown Structure):} Divides total work into clear, well-defined units/subtasks. Includes prerequisites and effort estimates.
    \item \textbf{Estimation:} Measured in man hour/day/month. Tasks must define exactly when they are "done".
    \item \textbf{Milestone:} End of stage indicating significant progress. Takes dependencies/priorities into account.
    \item \textbf{Buffer:} Time set aside for unforeseen delays.
    \item \textbf{Gantt Chart:} 2D bar-chart (Time vs Tasks horizontal bars). Tracks who/ongoing/done.
    \item \textbf{PERT Chart:} Graphical directed graph. Nodes = effort/tasks, Arrows = precedence/sequence.
\end{itemize}

\subsection{Team Structures}
\begin{itemize}
    \item \textbf{Egoless:} Every member equal in responsibility.
    \item \textbf{Chief Programmer:} Single authoritative figure directing.
    \item \textbf{Strict Hierarchy:} Tree system of strict organization.
\end{itemize}

\includegraphics[width=\linewidth]{img/facade.png}
\includegraphics[width=\linewidth]{img/uml-example-2.png}
\includegraphics[width=\linewidth]{img/uml-example-3.png}
\includegraphics[width=\linewidth]{img/uml-example-4.png}
% \includegraphics[width=\linewidth]{img/uml-example.png}
\includegraphics[width=\linewidth]{img/user-stories.png}
extreme
\includegraphics[width=\linewidth]{img/extreme-programming.png}
PERT
\includegraphics[width=\linewidth]{img/PERT-Network-Diagram.png}
Gannt
\includegraphics[width=\linewidth]{img/gannt chart.png}
State
\includegraphics[width=\linewidth]{img/state.png}
Communication
\includegraphics[width=\linewidth]{img/communication.png}
Timing
\includegraphics[width=\linewidth]{img/timing.png}

MISC
\begin{itemize}
    \item Defining APIs (Application Programming Interfaces) or "contracts" between components early in the design phase is a highly recommended best practice. It allows different teams (e.g., frontend and backend) to work in parallel
    \item While highly recommended for most projects, an architecture diagram is not strictly mandatory. 
    \item You should only use design patterns when they solve a specific problem you are facing. 
    \item While consulting customers is vital during the requirements gathering and user experience phases, the word "always" makes this tricky.
    \item ALT vs OPT ==> `if-else` or `switch`  VS `if` without else
    \item For the UML `loop`'s condition, if it is just a count (v<10), write `10 times` rather than a condition
    \item directed association is a subset of association
    \item indentation is 2 spaces instead of 4
    \item `git fetch` does not automatically merge changes unlike git pull. pull = fetch + merge
    \item In UML, generalization includes abstract classes.
    \item Security/Authentication: The listing module must require active session token authentication to ensure that only verified, logged-in users can add a bike to the system's database. (Relates to your "secure login" concept)
    \item Performance/Latency: The system must update the central database and display the newly listed bike in search results within 2 seconds of the owner submitting the listing. (Relates to your "live updates" concept)
    \item Both branch nodes and merge nodes in activity diagram are diamond shapes. Guard conditions must be in square brackets.
\end{itemize}

\begin{itemize}
    \item \textbf{Dependency}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A - - > B}
        \item \textbf{Meaning (A to B):} A uses B temporarily.
        \item \textbf{Additional Details:} This is the weakest relationship. It means A uses B in some way (e.g., B is a parameter in a method of A, or B is a local variable inside a method of A). If B changes, A might need to be updated, but A does not "hold" B as a permanent field.
    \end{itemize}

    \item \textbf{Association}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A - B}
        \item \textbf{Meaning (A to B):} A and B are linked (bidirectional).
        \item \textbf{Additional Details:} A structural relationship where both classes are aware of each other. They can communicate bidirectionally. Usually, this means both classes have a member variable (field) that references the other.
    \end{itemize}

    \item \textbf{Directed Assoc.}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A -> B}
        \item \textbf{Meaning (A to B):} A knows B (unidirectional).
        \item \textbf{Additional Details:} This defines "Navigability." Class A has a field/attribute of type B, but Class B does not have a reference to Class A. A can send messages to B, but not vice versa.
    \end{itemize}

    \item \textbf{Generalization}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A -$\triangleright$ B}
        \item \textbf{Meaning (A to B):} A is a type of B (Inheritance).
        \item \textbf{Additional Details:} A is a subclass (child) and B is the superclass (parent). A inherits all the attributes and methods of B. B is the more general concept, and A is the more specialized version.
    \end{itemize}

    \item \textbf{Realization}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A - - $\triangleright$ B}
        \item \textbf{Meaning (A to B):} A implements Interface B.
        \item \textbf{Additional Details:} B is typically an \textbf{Interface} or an Abstract Class. A provides the actual code (the "realization") for the methods defined in B.
    \end{itemize}

    \item \textbf{Aggregation}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A $\diamond$- B}
        \item \textbf{Meaning (A to B):} A contains B (B can survive alone).
        \item \textbf{Additional Details:} 
    \end{itemize}

    \item \textbf{Composition}
    \begin{itemize}
        \item \textbf{Visual Style:} \texttt{A $\blacklozenge$- B}
        \item \textbf{Meaning (A to B):} A owns B (B dies with A).
        \item \textbf{Additional Details:} 
    \end{itemize}
\end{itemize}

\end{multicols*}
\end{document}
```