import React, { useState } from 'react';
import './GoalTracker.css'; // Assuming the CSS is saved in this file

function GoalTracker() {
    const [goals, setGoals] = useState([]);
    const [newGoal, setNewGoal] = useState('');

    const addGoal = () => {
        if (!newGoal.trim()) return;
        const goal = {
            id: Math.random().toString(),
            text: newGoal,
            achieved: false,
        };
        setGoals([...goals, goal]);
        setNewGoal('');
    };

    const achieveGoal = (id) => {
        setGoals(goals.map(goal => {
            if (goal.id === id) {
                return { ...goal, achieved: !goal.achieved };
            }
            return goal;
        }));
    };

    return (
        <div className="goal-tracker">
            <h2>Goal Tracker</h2>
            <ul>
                {goals.map((goal) => (
                    <li key={goal.id} className={`goal ${goal.achieved ? 'achieved' : ''}`}>
                        {goal.text}
                        <button onClick={() => achieveGoal(goal.id)} className="achieve-button">
                            {goal.achieved ? 'Undo' : 'Complete'}
                        </button>
                    </li>
                ))}
            </ul>
            <div className="goal-input">
                <input
                    type="text"
                    placeholder="Add a new goal"
                    value={newGoal}
                    onChange={(e) => setNewGoal(e.target.value)}
                />
                <button onClick={addGoal}>Add Goal</button>
            </div>
        </div>
    );
}

export default GoalTracker;
s