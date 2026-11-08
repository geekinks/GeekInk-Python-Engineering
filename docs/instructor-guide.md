# Instructor Guide -- GeekInk Python Engineering

## Teaching Philosophy

GeekInk Python Engineering follows a project-based, community-driven learning model. Every concept is taught through practical application, not abstract theory. Students learn by building real software, collaborating with peers, and developing professional engineering habits from day one.

Core principles:

- **Build first, explain second.** Start each lesson with a working example, then unpack the concepts behind it.
- **Real problems, real tools.** Use scenarios students recognize: student records, local business inventory, community data. Use the same tools professionals use: Git, virtual environments, testing frameworks.
- **Gradual complexity.** Each day builds on the previous one. Never introduce more than one major new concept per lesson.
- **Engineering mindset.** Code quality, documentation, and collaboration are not add-ons taught in Module 9. They are habits reinforced from Day 1.
- **Inclusive and encouraging.** Students come from different backgrounds. Meet them where they are. Celebrate progress. Create a space where asking questions is expected.

---

## Program Structure

The 100-day curriculum is organized into 10 modules of 10 days each.

| Module | Days | Topic | Project Milestone |
| --- | --- | --- | --- |
| 01 | 1--10 | Python Foundations | Smart Personal Profile and Calculator |
| 02 | 11--20 | Data Structures and Problem Solving | Student Result Processing System |
| 03 | 21--30 | Functions, Modules and File Handling | Personal Expense Tracker |
| 04 | 31--40 | Object-Oriented Programming | Student Management System |
| 05 | 41--50 | Automation and Web Scraping | Automated Web Research Assistant |
| 06 | 51--60 | Database and Backend Engineering | Student Management REST API |
| 07 | 61--70 | GUI Application Development | Desktop Inventory Management App |
| 08 | 71--80 | Data Science and Visualization | Northern Nigeria Data Analysis Dashboard |
| 09 | 81--90 | Software Engineering Practices | Build, Test, Document and Deploy |
| 10 | 91--100 | AI, Machine Learning and Capstone | AI-Powered Capstone Project |

---

## Recommended Session Structure

Each day's lesson is designed for a 2-3 hour session. Adapt the timing to your cohort.

| Block | Duration | Activity |
| --- | --- | --- |
| Warm-up | 10 min | Review previous day's challenge. Ask 2-3 students to share their solutions. |
| Concept introduction | 20 min | Present the day's topic. Use the lesson README as your guide. |
| Live coding | 25 min | Walk through the Practical Examples section. Type the code live; do not just display it. |
| Guided practice | 25 min | Students work through the Guided Practice activity. Circulate and assist. |
| Break | 10 min | |
| Daily challenge | 30 min | Students attempt the Daily Challenge independently. |
| Review and reflection | 15 min | Discuss solutions. Ask reflection questions from the lesson. |
| Wrap-up | 5 min | Preview tomorrow's topic. Remind students of submission instructions. |

---

## Lesson Delivery Guidelines

1. **Prepare before each session.** Read the day's README. Run all code examples. Anticipate common errors students will encounter.
2. **Type code live.** Students learn more from watching you make and fix mistakes than from seeing finished code.
3. **Encourage questions.** If a student asks a question, assume others have the same question. Answer for the room.
4. **Use the board or screen for diagrams.** Concepts like loops, data structures, and OOP relationships benefit from visual explanation.
5. **Pair programming.** For complex exercises, pair weaker students with stronger ones. Rotate pairs regularly.
6. **Do not lecture for more than 20 minutes without coding.** If students are not typing, they are not learning.

---

## Assessment Framework

| Component | Weight | Description |
| --- | --- | --- |
| Conceptual understanding | 20% | Can the student explain why, not just how? Assessed through knowledge-check questions and reflection responses. |
| Practical implementation | 30% | Does the code work? Does it solve the problem as specified? |
| Code quality and engineering practices | 20% | PEP 8 compliance, meaningful names, proper structure, version control usage. |
| Project completion | 20% | Each module's milestone project, evaluated against its requirements. |
| Documentation and presentation | 10% | README quality, code comments where needed, ability to explain their work. |

### Performance Levels

| Level | Score Range | Description |
| --- | --- | --- |
| Excellent | 90--100 | Exceeds requirements. Clean code, thorough testing, clear documentation. |
| Good | 75--89 | Meets all requirements. Minor improvements possible. |
| Satisfactory | 60--74 | Meets core requirements. Notable gaps in quality or completeness. |
| Needs Improvement | Below 60 | Does not meet core requirements. Requires additional support and resubmission. |

---

## Module Milestone Evaluation

At the end of each module (Days 10, 20, 30, etc.), students submit a project. Evaluate using:

1. **Does it run?** The program should execute without errors for the expected use cases.
2. **Does it meet requirements?** Check against the project README's requirements list.
3. **Code quality.** Is the code organized? Are functions/classes used appropriately for the module level?
4. **Input handling.** Does it handle invalid input gracefully (for modules where this has been taught)?
5. **Documentation.** Does the submission include a README explaining what was built and how to run it?

Provide written feedback on every milestone submission. Be specific: "Your `calculate_grade` function handles edge cases well" is more useful than "Good job."

---

## Mentorship Expectations

- **Be available.** Designate office hours or a communication channel where students can ask questions outside sessions.
- **Track progress.** Review student submissions within 48 hours. Flag students who fall behind.
- **Encourage peer review.** Starting from Module 3, have students review each other's code before submitting.
- **Normalize struggle.** Programming is hard. When students are frustrated, remind them that debugging is a skill they are actively developing.
- **Celebrate milestones.** Acknowledge module completions publicly. Highlight creative or well-engineered solutions.

---

## Student Engagement Strategies

- **Daily challenges as competitions.** Optionally track who completes challenges first or most creatively.
- **Code walkthroughs.** Ask students to present their solutions to the class. This builds communication skills.
- **Real-world connections.** When teaching a concept, share how it is used in industry. "This is how inventory systems at shops work" makes dictionaries concrete.
- **Guest sessions.** Invite working developers to share their experience, especially those from Northern Nigeria's tech community.
- **Group projects.** For modules 6-10, consider assigning group projects alongside individual work to build collaboration skills.

---

## Git and GitHub Integration

Git is introduced formally in Module 9, but students should use it from Day 1 for submissions.

### Minimum Git skills by module:

| Module | Expected Git Usage |
| --- | --- |
| 1--3 | Fork, clone, create files, add, commit, push, submit PR |
| 4--6 | Branches, meaningful commit messages, .gitignore |
| 7--9 | Feature branches, PR descriptions, code review comments |
| 10 | Full workflow: branch, commit, PR, review, merge |

Provide a Git cheat sheet in the first session. Walk through the first PR submission as a class.

---

## Handling Different Skill Levels

- **Complete beginners:** Pair them with a peer. Spend extra time on Days 1-3 setup. Provide additional practice problems.
- **Students with some experience:** Challenge them with bonus requirements on daily challenges. Ask them to help peers.
- **Advanced students:** Direct them to the specialization tracks. Encourage them to contribute exercises back to the repository.

---

## Capstone Project Supervision (Module 10)

1. **Day 91-93:** Students propose their project. Review proposals for feasibility.
2. **Day 94-96:** Weekly check-ins on progress. Help unblock technical issues.
3. **Day 97-98:** Code review session. Students present work-in-progress.
4. **Day 99:** Final submission deadline.
5. **Day 100:** Presentations and technical defense.

Capstone evaluation criteria are detailed in `docs/capstone-guidelines.md`.

---

## Resources

- [Student Guide](student-guide.md)
- [Assessment Rubric](assessment-rubric.md)
- [Environment Setup](environment-setup.md)
- [Capstone Guidelines](capstone-guidelines.md)
- [Contributing Guide](../CONTRIBUTING.md)

---

## Financial Python Track

The original 3-week Financial Python curriculum is preserved as a specialization track. See `docs/instructor_guide.md` (the original financial track guide) and `specializations/financial-python/` for those materials.
