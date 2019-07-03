using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Predict_Grades
{
    public partial class root : Form
    {
        public root()
        {
            InitializeComponent();
        }

        private void startPredictBtn_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Predict");
        }

        private void newPredictBtn_Click(object sender, EventArgs e)
        {
            mockGradeEntry.Text = "";
            attendanceEntry.Text = "";

        }

        private void helpBtn_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("S:\\One Drive\\OneDrive - Cowes Enterprise College\\Machine Learning\\Predicting Grades (Front End)\\website_home.html");
        }
    }
}
