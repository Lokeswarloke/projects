import { useState } from "react";

const intialData = [
  {
    id: "1",
    description: "Salary",
    amount: 3000,
    category: "Income",
    date: "2024-09-01",
  },
  {
    id: "2",
    description: "Groceries",
    amount: 150,
    category: "Expense",
    date: "2024-09-02",
  },
  {
    id: "3",
    description: "Electricity Bill",
    amount: 75,
    category: "Expense",
    date: "2024-09-03",
  },
  {
    id: "4",
    description: "Freelance Work",
    amount: 500,
    category: "Income",
    date: "2024-09-05",
  },
  {
    id: "5",
    description: "Dining Out",
    amount: 60,
    category: "Expense",
    date: "2024-09-06",
  },
];

export default function App() {
  const [items, setItems] = useState([]);

  function handleAddItems(item) {
    setItems((currItems) => [...currItems, item]);
  }

  function handleDeleteItems(id) {
    console.log(id);
    setItems((currItems) => currItems.filter((item) => item.id !== id));
  }

  return (
    <div className="app">
      <div className="main-section">
        <ExpenseForm onAddItem={handleAddItems} />
        <ExpenseList onDelete={handleDeleteItems} itemsList={items} />
      </div>
      <Total items={items} />
    </div>
  );
}

function ExpenseForm({ onAddItem }) {
  const [desc, setDesc] = useState("");
  const [categ, setCateg] = useState("Income");
  const [amount, setAmount] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    if (!desc || !categ) return;

    const id = crypto.randomUUID();
    const newItems = {
      id: id,
      description: desc,
      category: categ,
      amount: categ === "Expense" ? -amount : amount,
    };

    console.log(newItems);
    onAddItem(newItems);
  }

  return (
    <div className="expense-form">
      <form onSubmit={handleSubmit}>
        <label>Description</label>
        <input
          type="text"
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
        />
        <br></br>
        <label>Category</label>
        <select value={categ} onChange={(e) => setCateg(e.target.value)}>
          <option value="Income">Income</option>
          <option value="Expense">Expense</option>
        </select>
        <br></br>
        <label>Amount</label>
        <input
          type="text"
          value={amount}
          onChange={(e) => setAmount(Number(e.target.value))}
        />
        <button>Submit</button>
      </form>
    </div>
  );
}

function ExpenseList({ onDelete, itemsList }) {
  return (
    <div className="list-wrapper">
      <ul>
        {itemsList.map((ele) => (
          <ExpenseItem
            description={ele.description}
            amount={ele.amount}
            category={ele.category}
            key={ele.id}
            onDelete={onDelete}
            id={ele.id}
          />
        ))}
      </ul>
    </div>
  );
}

function ExpenseItem({ description, amount, category, onDelete, id }) {
  return (
    <li
      style={
        category === "Expense"
          ? { backgroundColor: "#fa4604df" }
          : { backgroundColor: "#28a745" }
      }
    >
      <p>
        🆕{description} 💲{Math.abs(amount)} 💹{category}
      </p>
      <button onClick={() => onDelete(id)}>Delete</button>
    </li>
  );
}

function Total({ items }) {
  const income = items
    .filter((item) => item.amount > 0)
    .map((ele) => ele.amount)
    .reduce((acc, curr) => {
      return acc + curr;
    }, 0);
  console.log(income);
  const expense = items
    .filter((item) => item.amount < 0)
    .map((ele) => ele.amount)
    .reduce((acc, curr) => {
      return acc + Math.abs(curr);
    }, 0);
  console.log(expense);

  const balance = income - expense;

  return (
    <>
      {items.length > 0 ? (
        <div className="stats">
          <p>
            Balance:{" "}
            <span
              style={
                balance < 0 ? { color: "#fa4604df" } : { color: "#28a745" }
              }
            >
              {balance}
            </span>
          </p>
          <p>
            Total Income: <span>{income}</span>
          </p>
          <p>
            Total Expense: <span>{expense}</span>
          </p>
        </div>
      ) : null}
    </>
  );
}
