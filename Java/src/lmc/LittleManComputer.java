package lmc;

/**
 * The LittleManComputer itself
 * @author      Matthew Hopson
 * @version     1.0
 * @since       1.0
 */
public class LittleManComputer
{
    int[] memory;

    int programCounter;
    int instructionRegister;
    int addressRegister;
    int accumulator;

    public LittleManComputer(String file)
    {
        memory = new int[100]; //LMC has 100 memory locations
        programCounter = 0;
        instructionRegister = -1;
        addressRegister = 0;
        accumulator = 0;

        Assembler assembler = new Assembler(memory);
        assembler.assemble(file);
    }

    /**
     * runs the computer
     */
    public void run()
    {
        while(instructionRegister != 0) {
            if (!fetchNextInstruction()) {
                break;
            }
            executeInstruction();
            System.out.printf("Instruction: %d, Address: %d\n", instructionRegister, addressRegister);
        }
    }

    /**
     * Loads the next instruction into the registers
     * @return whether or not it is the end of the instructions
     */
    private boolean fetchNextInstruction()
    {
        int opcode = memory[programCounter++];
        String opString = String.valueOf(opcode);

        String instruction = "" + opString.charAt(0);
        if (instruction.equals("0")) {
            return false;
        }
        String address     = "" + opString.charAt(1) + opString.charAt(2);

        instructionRegister = Integer.parseInt(instruction);
        addressRegister     = Integer.parseInt(address);
        return true;
    }

    private void add()
    {

    }

    private void subtract()
    {

    }

    private void store()
    {

    }

    private void load()
    {

    }

    private void branch(boolean condition)
    {

    }

    private void input()
    {

    }

    private  void output()
    {

    }


    /**
     * Executes the instruction at the
     * @return whether or not it is the end of the instructions
     */
    private void executeInstruction()
    {
        switch (instructionRegister) {
            case 1:
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;
            case 6:
                break;
            case 7:
                break;
            case 8:
                break;
            case 9:
                break;
        }
    }
}
