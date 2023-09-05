export type Message = {
    id: string
    Personality: Personality | null
    personalityId: string | null
    sender: string
    content: string
    createdAt: Date
    updatedAt: Date
  }
  
  export type Personality = {
    id: string
    name: string
    age: number
    gender: string
    DOB: Date
    Description: string
    // Messages: Message[]
    createdAt: Date
    updatedAt: Date
  }