import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class RockPaperScissorsUI extends JFrame implements ActionListener {

    private JLabel resultLabel;

    public RockPaperScissorsUI() {
        // Set up the frame
        setTitle("Rock, Paper, Scissors Game");
        setSize(300, 150);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Create components
        resultLabel = new JLabel("Choose Rock, Paper, or Scissors");

        JButton rockButton = new JButton("Rock");
        JButton paperButton = new JButton("Paper");
        JButton scissorsButton = new JButton("Scissors");

        // Add action listeners
        rockButton.addActionListener(this);
        paperButton.addActionListener(this);
        scissorsButton.addActionListener(this);

        // Add components to the frame
        add(resultLabel, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(rockButton);
        buttonPanel.add(paperButton);
        buttonPanel.add(scissorsButton);

        add(buttonPanel, BorderLayout.CENTER);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String userChoice = e.getActionCommand();
        String[] choices = {"Rock", "Paper", "Scissors"};
        Random random = new Random();
        int computerIndex = random.nextInt(3);
        String computerChoice = choices[computerIndex];

        determineWinner(userChoice, computerChoice);
    }

    private void determineWinner(String userChoice, String computerChoice) {
        if (userChoice.equalsIgnoreCase(computerChoice)) {
            resultLabel.setText("It's a tie!");
        } else if ((userChoice.equalsIgnoreCase("Rock") && computerChoice.equalsIgnoreCase("Scissors"))
                || (userChoice.equalsIgnoreCase("Paper") && computerChoice.equalsIgnoreCase("Rock"))
                || (userChoice.equalsIgnoreCase("Scissors") && computerChoice.equalsIgnoreCase("Paper"))) {
            resultLabel.setText("You win!");
        } else {
            resultLabel.setText("Computer wins!");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            RockPaperScissorsUI gameUI = new RockPaperScissorsUI();
            gameUI.setVisible(true);
        });
    }
}                