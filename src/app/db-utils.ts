import { PrismaClient } from "@prisma/client";
import { prisma } from "./db";
import { Personality, Message } from "./types";


export async function getPersonalies(): Promise<Personality[]> {
    return await prisma.personality.findMany()
}

export async function getPersonality(id: string) {
    return await prisma.personality.findUnique({where: {id: id}})
}

export async function addPersonality(personality: Personality) {
    await prisma.personality.create({data: personality})
}