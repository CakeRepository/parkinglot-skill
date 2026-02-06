import argparse
import os

def run_consensus(query: str, max_retries: int = 3):
    """
    Simulates a debate between two agents to refine a plan.
    """
    current_plan = query
    confidence_score = 0
    retries = 0

    while confidence_score < 90 and retries < max_retries:
        print(f"--- Iteration {retries + 1} ---")

        # Agent A (Critique)
        critique_prompt = f"Critique the following plan: {current_plan}"
        print(f"Agent A (Critique): {critique_prompt}")

        # Agent B (Solve)
        # Simulate Agent B generating a new plan based on the critique.
        # The key is that this "solution" should not recursively embed the critique prompt
        # if the intent is for current_plan to be the refined output.
        # Let's simplify the 'solution' itself to prevent the accumulation.
        # In a real scenario, this 'solution' would be the actual refined plan from Agent B.
        solution = f"Refined plan based on '{query}' (Iteration {retries + 1})"
        print(f"Agent B (Solve): {solution}")
        current_plan = solution # The new plan is the result of Agent B's work

        # Judge
        # In a real scenario, this would involve a call to an LLM or a more complex evaluation.
        # Here, we'll simulate the judge's decision.
        # The judge's confidence score should also be based on the *actual* current_plan, not the prompt.
        if "refined" in current_plan.lower():
            confidence_score += 30
        if "iteration" in current_plan.lower():
            confidence_score += 10
        
        # for real implementation, we can use another model to judge the confidence score
        confidence_score = min(100, confidence_score) 

        print(f"Judge: Confidence Score = {confidence_score}%")
        
        if confidence_score < 90:
            print("The solution is not confident enough. Continuing the debate.")
        else:
            print("The solution is confident enough. Ending the debate.")

        retries += 1
        print()

    print("--- Final Solution ---")
    print(current_plan)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parking Lot Consensus Tool")
    parser.add_argument("query", type=str, help="The initial query or plan.")
    args = parser.parse_args()
    run_consensus(args.query)
