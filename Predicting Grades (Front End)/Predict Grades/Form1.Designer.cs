namespace Predict_Grades
{
    partial class root
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.header = new System.Windows.Forms.Panel();
            this.helpBtn = new System.Windows.Forms.Button();
            this.newPredictBtn = new System.Windows.Forms.Button();
            this.titleLbl = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.startPredictBtn = new System.Windows.Forms.Button();
            this.mockGradeEntry = new System.Windows.Forms.TextBox();
            this.attendanceEntry = new System.Windows.Forms.TextBox();
            this.mockGradeLbl = new System.Windows.Forms.Label();
            this.attendanceLbl = new System.Windows.Forms.Label();
            this.bottomPannel = new System.Windows.Forms.Panel();
            this.header.SuspendLayout();
            this.SuspendLayout();
            // 
            // header
            // 
            this.header.BackColor = System.Drawing.Color.Maroon;
            this.header.Controls.Add(this.helpBtn);
            this.header.Controls.Add(this.newPredictBtn);
            this.header.Controls.Add(this.titleLbl);
            this.header.Controls.Add(this.label1);
            this.header.Dock = System.Windows.Forms.DockStyle.Top;
            this.header.Location = new System.Drawing.Point(0, 0);
            this.header.Name = "header";
            this.header.Size = new System.Drawing.Size(800, 85);
            this.header.TabIndex = 0;
            // 
            // helpBtn
            // 
            this.helpBtn.Location = new System.Drawing.Point(135, 54);
            this.helpBtn.Name = "helpBtn";
            this.helpBtn.Size = new System.Drawing.Size(75, 23);
            this.helpBtn.TabIndex = 3;
            this.helpBtn.Text = "Help";
            this.helpBtn.UseVisualStyleBackColor = true;
            this.helpBtn.Click += new System.EventHandler(this.helpBtn_Click);
            // 
            // newPredictBtn
            // 
            this.newPredictBtn.Location = new System.Drawing.Point(12, 54);
            this.newPredictBtn.Name = "newPredictBtn";
            this.newPredictBtn.Size = new System.Drawing.Size(115, 23);
            this.newPredictBtn.TabIndex = 2;
            this.newPredictBtn.Text = "New Prediction";
            this.newPredictBtn.UseVisualStyleBackColor = true;
            this.newPredictBtn.Click += new System.EventHandler(this.newPredictBtn_Click);
            // 
            // titleLbl
            // 
            this.titleLbl.AutoSize = true;
            this.titleLbl.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.titleLbl.Location = new System.Drawing.Point(12, 9);
            this.titleLbl.Name = "titleLbl";
            this.titleLbl.Size = new System.Drawing.Size(382, 27);
            this.titleLbl.TabIndex = 1;
            this.titleLbl.Text = "Grade Predictor Using Machine Learning";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 13);
            this.label1.TabIndex = 0;
            // 
            // startPredictBtn
            // 
            this.startPredictBtn.BackColor = System.Drawing.Color.Maroon;
            this.startPredictBtn.Font = new System.Drawing.Font("Comic Sans MS", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.startPredictBtn.Location = new System.Drawing.Point(534, 137);
            this.startPredictBtn.Name = "startPredictBtn";
            this.startPredictBtn.Size = new System.Drawing.Size(160, 89);
            this.startPredictBtn.TabIndex = 1;
            this.startPredictBtn.Text = "Predict Grades";
            this.startPredictBtn.UseVisualStyleBackColor = false;
            this.startPredictBtn.Click += new System.EventHandler(this.startPredictBtn_Click);
            // 
            // mockGradeEntry
            // 
            this.mockGradeEntry.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mockGradeEntry.Location = new System.Drawing.Point(212, 137);
            this.mockGradeEntry.Name = "mockGradeEntry";
            this.mockGradeEntry.Size = new System.Drawing.Size(245, 34);
            this.mockGradeEntry.TabIndex = 2;
            // 
            // attendanceEntry
            // 
            this.attendanceEntry.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.attendanceEntry.Location = new System.Drawing.Point(212, 192);
            this.attendanceEntry.Name = "attendanceEntry";
            this.attendanceEntry.Size = new System.Drawing.Size(245, 34);
            this.attendanceEntry.TabIndex = 3;
            // 
            // mockGradeLbl
            // 
            this.mockGradeLbl.AutoSize = true;
            this.mockGradeLbl.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mockGradeLbl.Location = new System.Drawing.Point(46, 140);
            this.mockGradeLbl.Name = "mockGradeLbl";
            this.mockGradeLbl.Size = new System.Drawing.Size(124, 26);
            this.mockGradeLbl.TabIndex = 4;
            this.mockGradeLbl.Text = "Mock Grade:";
            // 
            // attendanceLbl
            // 
            this.attendanceLbl.AutoSize = true;
            this.attendanceLbl.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.attendanceLbl.Location = new System.Drawing.Point(49, 195);
            this.attendanceLbl.Name = "attendanceLbl";
            this.attendanceLbl.Size = new System.Drawing.Size(118, 26);
            this.attendanceLbl.TabIndex = 5;
            this.attendanceLbl.Text = "Attendance:";
            // 
            // bottomPannel
            // 
            this.bottomPannel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.bottomPannel.Location = new System.Drawing.Point(12, 272);
            this.bottomPannel.Name = "bottomPannel";
            this.bottomPannel.Size = new System.Drawing.Size(776, 166);
            this.bottomPannel.TabIndex = 6;
            // 
            // root
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.bottomPannel);
            this.Controls.Add(this.header);
            this.Controls.Add(this.attendanceLbl);
            this.Controls.Add(this.mockGradeLbl);
            this.Controls.Add(this.attendanceEntry);
            this.Controls.Add(this.mockGradeEntry);
            this.Controls.Add(this.startPredictBtn);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.Name = "root";
            this.Text = "Grade Predictor";
            this.header.ResumeLayout(false);
            this.header.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel header;
        private System.Windows.Forms.Button startPredictBtn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox mockGradeEntry;
        private System.Windows.Forms.TextBox attendanceEntry;
        private System.Windows.Forms.Label mockGradeLbl;
        private System.Windows.Forms.Label attendanceLbl;
        private System.Windows.Forms.Button helpBtn;
        private System.Windows.Forms.Button newPredictBtn;
        private System.Windows.Forms.Label titleLbl;
        private System.Windows.Forms.Panel bottomPannel;
    }
}

