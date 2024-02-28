import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addGoal, toggleGoalAchieved } from '../../actions/goalActions'; // Import your goal actions
import './GoalTracker.css';


function GoalTracker() {
    const [newGoalText, setNewGoalText] = useState('');
    const goals = useSelector(state => state.goal.goals); // Access goals from Redux store
    const dispatch = useDispatch();

    const handleAddGoal = () => {
        if (!newGoalText.trim()) return;
        // Dispatch the action to add a goal
        dispatch(addGoal({ id: Math.random().toString(), text: newGoalText, achieved: false }));
        setNewGoalText('');
    };

    const handleAchieveGoal = (id) => {
        // Dispatch an action to toggle the 'achieved' state of the goal
        dispatch(toggleGoalAchieved(id));
    };

    return (
        <div className="goal-tracker">
            <h2>Goal Tracker</h2>
            <ul>
                {goals.map((goal) => (
                    <li key={goal.id} className={`goal ${goal.achieved ? 'achieved' : ''}`}>
                        {goal.text}
                        <button onClick={() => handleAchieveGoal(goal.id)} className="achieve-button">
                            {goal.achieved ? 'Undo' : 'Complete'}
                        </button>
                    </li>
                ))}
            </ul>
            <div className="goal-input">
                <input
                    type="text"
                    placeholder="Add a new goal"
                    value={newGoalText}
                    onChange={(e) => setNewGoalText(e.target.value)}
                />
                <button onClick={handleAddGoal}>Add Goal</button>
            </div>
        </div>
    );
}

export default GoalTracker;
