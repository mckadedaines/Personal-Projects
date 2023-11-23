const promptElement = document.querySelector("#question_prompt");
const answersElement = document.querySelector(".answers");

let questions = [
        {
            question: "What is the capital of France?",
            answers: [
                { text: "A) Berlin", isCorrect: false },
                { text: "B) London", isCorrect: false },
                { text: "C) Paris", isCorrect: true },
                { text: "D) Rome", isCorrect: false }
            ]
        },
        {
            question: "What color do you get when you mix red and yellow?",
            answers: [
                { text: "A) Orange", isCorrect: true },
                { text: "B) Purple", isCorrect: false },
                { text: "C) Green", isCorrect: false },
                { text: "D) Blue", isCorrect: false }
            ]
        },
        {
            question: "How many continents are there on Earth?",
            answers: [
                { text: "A) 5", isCorrect: false },
                { text: "B) 6", isCorrect: false },
                { text: "C) 7", isCorrect: true },
                { text: "D) 8", isCorrect: false }
            ]
        },
        {
            question: "What is the largest planet in our solar system?",
            answers: [
                { text: "A) Earth", isCorrect: false },
                { text: "B) Mars", isCorrect: false },
                { text: "C) Jupiter", isCorrect: true },
                { text: "D) Saturn", isCorrect: false }
            ]
        },
        {
            question: "Which animal is known as the 'King of the Jungle'?",
            answers: [
                { text: "A) Elephant", isCorrect: false },
                { text: "B) Lion", isCorrect: true },
                { text: "C) Tiger", isCorrect: false },
                { text: "D) Gorilla", isCorrect: false }
            ]
        },
        {
            question: "What gas do plants absorb from the air for photosynthesis?",
            answers: [
                { text: "A) Oxygen", isCorrect: false },
                { text: "B) Nitrogen", isCorrect: false },
                { text: "C) Carbon Dioxide", isCorrect: true },
                { text: "D) Hydrogen", isCorrect: false }
            ]
        },
        {
            question: "What is the boiling point of water?",
            answers: [
                { text: "A) 100 degrees Celsius", isCorrect: true },
                { text: "B) 90 degrees Celsius", isCorrect: false },
                { text: "C) 80 degrees Celsius", isCorrect: false },
                { text: "D) 110 degrees Celsius", isCorrect: false }
            ]
        },
        {
            question: "Which of these is not a primary color?",
            answers: [
                { text: "A) Red", isCorrect: false },
                { text: "B) Blue", isCorrect: false },
                { text: "C) Green", isCorrect: true },
                { text: "D) Yellow", isCorrect: false }
            ]
        },
        {
            question: "Who wrote the play 'Romeo and Juliet'?",
            answers: [
                { text: "A) Charles Dickens", isCorrect: false },
                { text: "B) Jane Austen", isCorrect: false },
                { text: "C) William Shakespeare", isCorrect: true },
                { text: "D) Mark Twain", isCorrect: false }
            ]
        },
        {
            question: "What is the largest mammal in the world?",
            answers: [
                { text: "A) Elephant", isCorrect: false },
                { text: "B) Giraffe", isCorrect: false },
                { text: "C) Blue Whale", isCorrect: true },
                { text: "D) Rhinoceros", isCorrect: false }
            ]
        }
    ];

let randomIndex = Math.floor(Math.random() * questions.length);
let selectedQuestion = questions[randomIndex];

promptElement.textContent = selectedQuestion.question;

answersElement.innerHTML = '';

function setupQuestion() {
    let randomIndex = Math.floor(Math.random() * questions.length);
    let selectedQuestion = questions[randomIndex];

    promptElement.textContent = selectedQuestion.question;

    answersElement.innerHTML = '';

    selectedQuestion.answers.forEach(answer => {
        let answerElement = document.createElement("div");
        answerElement.className = "answers-box";
        answerElement.textContent = answer.text;

        answerElement.addEventListener("click", function() {
            // Disable further clicks
            document.querySelectorAll('.answers-box').forEach(box => {
                box.style.pointerEvents = 'none';
            });

            // Highlight correct and incorrect answers
            document.querySelectorAll('.answers-box').forEach((box, idx) => {
                if (selectedQuestion.answers[idx].isCorrect) {
                    box.style.backgroundColor = 'green';
                } else {
                    box.style.backgroundColor = 'red';
                }
            });

            // Alert and set up next question
            setTimeout(() => {
                if (answer.isCorrect) {
                    alert("Correct!");
                } else {
                    alert("Wrong answer");
                }
                setupQuestion(); // Set up the next question
            }, 300); // Delay to allow answer highlighting to be seen
        });

        answersElement.appendChild(answerElement);
    });
}

setupQuestion(); // Initialize the first question