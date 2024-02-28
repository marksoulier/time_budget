// goalActions.js

// Action Types
export const ADD_GOAL = 'ADD_GOAL';
export const REMOVE_GOAL = 'REMOVE_GOAL';
// Add this to your existing action types
export const TOGGLE_GOAL_ACHIEVED = 'TOGGLE_GOAL_ACHIEVED';


// Action Creators

// Add a Goal
export const addGoal = (goal) => ({
    type: ADD_GOAL,
    payload: goal,
});

// Remove a Goal by id
export const removeGoal = (id) => ({
    type: REMOVE_GOAL,
    payload: id,
});


// Add this function to goalActions.js
export const toggleGoalAchieved = (id) => ({
    type: TOGGLE_GOAL_ACHIEVED,
    payload: id,
});
