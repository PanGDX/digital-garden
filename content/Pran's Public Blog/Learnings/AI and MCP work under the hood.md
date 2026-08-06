# Sources and Inspiration
https://www.youtube.com/watch?v=GrNbuWWJYiI&pp=ugUHEgVlbi1VUw%3D%3D

# Explanation
The below diagram captures a great picture of the overview of how real AI systems are implemented. 
![[Pasted image 20260806113610.png]]

Source: https://www.youtube.com/watch?v=GrNbuWWJYiI&pp=ugUHEgVlbi1VUw%3D%3D

The video gives a great explanation of how the loop works but does not go into detail for any specific point.
Going from left to right, we start at `User Prompt`, `Current Chat History` and `System Prompt`. These are the starting bricks that feed into the working memory. The working memory is what is being sent to the LLM. However, it is often the case that this context is insufficient. The reason for this is because these three bricks create the question to be asked and the scope of answering but does not give grounding to the LLM. Grounding the LLM is very important to prevent hallucinations. To ground it, we provide `Skills.md` or clear steps to build or design the solution. You can often download these skills from Github or build your own based on existing workflows.
Relevant questions
> What happens when you have a lot of Skills.md? Does it get injected all at once or chosen based on the right context? How are the right Skills chosen?

With these four starting bricks, the programmer should be concerned about managing the context window and managing versions of the system prompt and Skills.md.
> Keeping a Git-like system of prompts through an integrated system like Langfuse is very valuable in keeping track of the best performing prompts

> Managing the context window is a crucial step here. As research shows, long context windows quickly degrade the performance of the LLM's answering capability. Managing the right Skills.md to inject into the system, managing the length of the system prompt and summarising the current chat window when the chat becomes too long are essential steps

The context problem does not end there. In reality when we want to use LLM for real world solutions, real enterprise or local data must be provided to the LLM's context. This comes from two places - `Semantic memory` and `Episodic memory`. Both employ RAG but are deeply different. `Semantic Memory` can be considered the 'truth' memory. These are pdf documents of internal workflows, real customer complaints formatted in XLSX files and more. This is stored in a vector database and then retrieved through RAG calls to provide relevant context to ground the output. For instance, if the executive asks "What is the most common pain points of customers based on the customer feedback", the system would use that question to query RAG and attempt to retrieve the relevant context
Here, the programmer has to be concerned with:

> The infrastructure surrounding the RAG's deployment which has to be poised to provide:
> Good uptime and response time per 1 query
> What happens if there are 1000 queries? Can batching be done? 
> How are questions classified and how are RAG queries written?
> What happens if the context retrieved is insufficient or not relevant?
> What are the top-k and prefetch-k values?
> How is the data extracted from documents? What types of documents are being fed into the system? PDF with text? PDF with pictures? Excel files? Slides? PNGs? 
> How can the RAG provide user profile? Or is the user profile provided in another manner?
> Identify the data sources and the accuracy of the data being fed into the system. Garbage in garbage out.
> What type of RAG is being used? Is it single retrieval? Multiple retrieval? Graph RAG?

Next is `Episodic Memory` which is concerned with dated events and past chat history. This is less concerned with facts from persistent documents but rather concerned with dated events. For example, AI chat history with a customer or non-AI system events like a customer filing feedback. The key concept here is providing the most recent context available. Let's say the user asks "Give me the last 10 negative feedback from customers", `Semantic memory` is unable to answer this because it does not contain such memory. However, by using vector stores and SQL DB, you can answer this question as the feedback data is stored inside the SQL DB. Notice that this episodic memory will use much more storage than semantic memory because it is constantly being updated as users feed in more data.

The programmer has to be concerned with
> How am I storing the data?
> How am I retrieving the data?
> Recognising that there is no perfect solution, the system cannot answer every granular question. Instead, the programmer has to work closely with the customer to set clear user requirements.
> How are dates stored? What other meta data are stored? How are they used in retrieval? Can a more deterministic system of filtering be used rather than simply using semantic search? For instance, if a question asks "Go through the month of April and summarise the negative feedback", can the system filter the date deterministically? Perhaps a sentiment tag can be attached to each feedback too. Such implements are now getting detailed and goes back to the question of 'what are the user requirements'.

After episodic memory is collated, there should be a summarizer agent that distills the memory into facts and feed it through a pipeline back into the semantic memory system.

Using both semantic and episodic memory raises the question of which context is prioritized and to what extent? 
> Should the system pull more semantic memory through a higher top-k? Or should the episodic memory pull more?

This builds the context. The context is then fed into the LLM. There are details here too

> What happens if there are 100, 1000 concurrent users? Each build their context and then feeds into the system but if requests are done one by one it is very inefficient. Instead, batching must be done. If the implementation uses local LLM, this is a real concern because batching is not inherently implemented.

Ok, now the LLM is generating answers. What if we want the LLM to do something beyond just providing an answer? Such as executing or writing code, modifying a database or sending messages? This goes into tool calling. Tool calling concerns the MCP framework which is a universal system for AI to call tools, much like how programmers would call REST API. MCPs are the arms to the LLM's brain. An LLM cannot magically connect and modify a company's SQL database but when it is connected to an MCP, this is possible. 

MCP is not magic. It is often deterministic, boring code that runs a certain function like `getEmployeeWage` or `sendSlackMessage`. This can then be connected to an external API layer again.

How does the LLM know what tool to use and what function to run? Each MCP must have a tool description and each function in the MCP contains the function's purpose. This is then fed into the LLM to let the LLM choose.

> Oh but how does the LLM know to call the tool correctly? What if it calls the wrong tool or the wrong parameters? 

> This is real and valid concern. Newer LLMs are trained against a tool calling system which have a fixed format based on the JSON format and parameters. They are penalized on wrong tool calls (wrong parameters, wrong JSON format) and rewarded on right tool calls. 
> The problem still exist however. There are five problems
> Wrong Name - calling `add_entry` instead of `add_entries`
> Wrong Tool - calling `delete` instead of `add` and thus executing the wrong tool call. This can be disastrous
> Hallucinated Arguments - using the right parameters but generating hallucinated arguments like fake users or ID
> Missing Key Parameters - missing key parameters such as ID and causing the code to crash
> Tool Bypass - ignoring the tool calling and instead generating hallucinated answers

> The solution? Three layers of defense
> Strict Schema validation - Use strictly typed schema that ensures that the input is formatted correctly before any code is ran. It is better to return a parameter error than to clean up the mess after a wrong tool call.
> Tool Whitelisting - Restrict the tool to only use pre-approved list of tools. This ensures that excessive tool agency is avoided as the programmer limits the tools available to 'harmless' tools - no tools that can delete an entire database
> Observability - Logging everything.


When dealing with MCP, here are the primary concerns
> What happens when you have 10 or 100 MCPs? How is the context window managed? How do you choose the right MCP tool's context to feed into the LLM's context. A viable solution is adding an MCP Selector Layer
> What happens if you have 100 MCP tool calls? If done sequentially, it will take ages. The solution? Batching and other optimization techniques
> Writing deterministic code in the MCP tool with clear execution flow and error handling. The tool should not have excessive power over any sensitive systems
> 
> https://www.cdata.com/blog/proven-mcp-performance-optimization-techniques

The next concept is the loop. It is often the case that multiple tool calls are necessary for a single task to be completed. The keyword here is completion. The loop's main concept is setting a clear 'completion' and 'break' condition. With an unclear completion criteria, the system can loop endlessly or excessively, calling the same tool dozens of times. 

> Setting a clear completion criteria for each task. Claude users will recall how the web UI will often ask the user to clarify the constraints of the task, giving generated option or letting the user put in their own answer. This is part of the loop.
> Setting a clear break case. How many tool calls are too many? There should be an upperbound that is tried and tested. Too low and no real useful output can be derived but too high and suddenly you are spending hundreds of dollars on LLM tool calls.

Finally, output!

Is this the end?

Not even close.

Much like how when you write code, you should have unit tests, the same concept applies to LLM but to an even greater extent. Because LLMs are an inherently deterministic system, it is crucial to trace every call. Tools like Langfuse and Langsmith are useful in doing so as they can cover the entire call chain, from the user prompt to RAG calls to LLM calls and to the output. 

The programmer should then evaluate based on two criterias
> Is the system healthy? How many tokens are being used per call? How many tool call? What is the response time and delay? What are the common errors encountered and are they important to address?
  
> Is the system good? Given the user requirements and a set of questions, evaluate the output and provide a score. Is the output accurate? Is the retrieved context relevant and useful.
> Langfuse can be used for this, but I prefer Promptfoo which has a lot of customizability, allowing for determinstic checks like ReGex and True/False evaluations as well as 'LLM as a Judge'

After that, evaluate what went wrong because there will definitely be something going wrong (I swear). Evaluate back against the user requirement - does it fall under the scope? Remember, not building a perfect system, building a precise system!

Based on the errors, deploy fixes
> Infrastructure changes to decrease latency
> Prompt changes to Skills.md or system prompts
> Change model configs, rate limits, tool permissions
> Modify MCP tool code
> Changing RAG parameters
> And much much more

That's a rundown of building out an AI Agent Harness with clear LLM Ops. This is not even including the deployment that encompasses Kubernetes or local deployment techniques. This is also not touching on the AI Security and Management side of things which is another entire package to unpack (See ISO42001) 